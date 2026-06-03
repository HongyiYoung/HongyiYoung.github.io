Jekyll::Hooks.register :site, :after_init do |site|
  require 'css_parser'
  require 'digest'
  require 'fileutils'
  require 'nokogiri'
  require 'open-uri'
  require 'tempfile'
  require 'uri'

  font_file_types = ['otf', 'ttf', 'woff', 'woff2']
  image_file_types = ['.gif', '.jpg', '.jpeg', '.png', '.webp']

  def local_asset_path(config, dirname, file_name)
    baseurl = config['baseurl'].to_s
    if baseurl.empty?
      File.join('/assets', 'libs', dirname, file_name)
    else
      File.join(baseurl, 'assets', 'libs', dirname, file_name)
    end
  end

  def normalize_asset_url(url, source_url = nil)
    if url.start_with?('//')
      "https:#{url}"
    elsif url.start_with?('http://', 'https://')
      url
    else
      URI.join(source_url || '', url).to_s
    end
  end

  def extract_css_url(value)
    match = value.match(/url\((['"]?)([^'")]+)\1\)/)
    match && match[2]
  end

  def download_and_change_rule_set_url(rule_set, rule, dest, dirname, config, file_types, source_url = nil)
    # check if the rule has a url
    if rule_set[rule]&.include?('url(')
      previous_rule = rule_set[rule]
      changed_values = []
      downloadable_values = 0
      downloaded_values = 0

      previous_rule.split(',').each do |source_part|
        url = extract_css_url(source_part)
        unless url
          changed_values << source_part.strip
          next
        end

        file_name = url.split('/').last.split('?').first
        unless file_name.end_with?(*file_types)
          changed_values << source_part.strip
          next
        end

        downloadable_values += 1
        absolute_url = normalize_asset_url(url, source_url)

        begin
          download_file(absolute_url, File.join(dest, file_name))
          local_url = local_asset_path(config, dirname, file_name)
          changed_values << source_part.sub(/url\((['"]?)([^'")]+)\1\)/, "url(#{local_url})").strip
          downloaded_values += 1
        rescue OpenURI::HTTPError, SocketError, SystemCallError => e
          warn "Skipping unavailable font source #{absolute_url}: #{e.message}"
        end
      end

      if downloadable_values.positive? && downloaded_values.zero?
        raise "Failed to download any usable font sources from #{previous_rule}"
      end

      if downloaded_values.positive?
        rule_set[rule] = changed_values.join(', ')
        puts "Changed #{previous_rule} to #{rule_set[rule]}"
      end
    end
  end

  def download_file(url, dest)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # create the directory if it doesn't exist
    dir = File.dirname(dest)
    unless File.directory?(dir)
      FileUtils.mkdir_p(dir)
    end

    # download the file if it doesn't exist
    unless File.file?(dest) && File.size?(dest)
      FileUtils.rm_f(dest) if File.file?(dest) && !File.size?(dest)
      puts "Downloading #{url} to #{dest}"
      tmp_file = Tempfile.new(['download-3rd-party', File.extname(dest)], dir)
      begin
        URI(url).open("rb") do |read_file|
          tmp_file.write(read_file.read)
        end
        tmp_file.close
        FileUtils.mv(tmp_file.path, dest)
      ensure
        tmp_file.close unless tmp_file.closed?
        tmp_file.unlink if File.exist?(tmp_file.path)
      end

      # check if the file was downloaded successfully
      unless File.file?(dest) && File.size?(dest)
        raise "Failed to download #{url} to #{dest}"
      end
    end
  end

  def replace_file_text(path, replacements)
    return unless File.file?(path)

    content = File.read(path)
    updated = content.dup
    replacements.each do |from, to|
      updated = updated.gsub(from, to)
    end
    File.write(path, updated) if updated != content
  end

  def download_fonts(url, dest, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # only download fonts if the directory doesn't exist or is empty
    unless File.directory?(dest) && !Dir.empty?(dest)
      puts "Downloading fonts from #{url} to #{dest}"
      # get available fonts from the url
      doc = Nokogiri::HTML(URI(url).open("User-Agent" => "Ruby/#{RUBY_VERSION}"))
      doc.css('a').each do |link|
        # get the file name from the url
        file_name = link['href'].split('/').last.split('?').first

        # verify if the file is a font file
        if file_name.end_with?(*file_types)
          # download the file and change the url to the local file
          download_file(URI.join(url, link['href']).to_s, File.join(dest, file_name))
        end
      end
    end
  end

  def download_images(url, dest, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # only download images if the directory doesn't exist or is empty
    unless File.directory?(dest) && !Dir.empty?(dest)
      puts "Downloading images from #{url} to #{dest}"
      # get available fonts from the url
      doc = Nokogiri::HTML(URI(url).open("User-Agent" => "Ruby/#{RUBY_VERSION}"))
      doc.xpath('/html/body/div/div[3]/table/tbody/tr/td[1]/a').each do |link|
        # get the file name from the url
        file_name = link['href'].split('/').last.split('?').first

        # verify if the file is a font file
        if file_name.end_with?(*file_types)
          # download the file and change the url to the local file
          download_file(URI.join(url, link['href']).to_s, File.join(dest, file_name))
        end
      end
    end
  end

  def download_fonts_from_css(config, url, dest, lib_name, file_types)
    # only try to download the file if url doesn't start with | for security reasons
    if url.start_with?('|')
      return
    end

    # get the file name from the url
    file_name = url.split('/').last.split('?').first

    if file_name == 'css'
      file_name = 'google-fonts.css'
    end

    # only download the css file if it doesn't exist
    unless File.file?(File.join(dest, file_name))
      puts "Downloading fonts from #{url} to #{dest}"
      # download the css file with a fake user agent to force downloading woff2 fonts instead of ttf
      # user agent from https://www.whatismybrowser.com/guides/the-latest-user-agent/chrome
      doc = Nokogiri::HTML(URI(url).open("User-Agent" => "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"))
      css = CssParser::Parser.new
      css.load_string! doc.document.text

      # get the font-face rules
      css.each_rule_set do |rule_set|
        # check if the rule set has a url
        download_and_change_rule_set_url(rule_set, 'src', File.join(dest, 'fonts'), File.join(lib_name, 'fonts'), config, file_types, url)
      end

      # save the modified css file
      puts "Saving modified css file to #{File.join(dest, file_name)}"
      File.write(File.join(dest, file_name), css.to_s)
    end

    return file_name
  end

  # replace {{version}} with the version number in all 3rd party libraries urls
  site.config['third_party_libraries'].each do |key, value|
    if key != 'download'
      value['url'].each do |type, url|
        # check if url is a dictionary
        if url.is_a?(Hash)
          url.each do |type2, url2|
            # replace {{version}} with the version number if it exists
            if url2.include?('{{version}}')
              site.config['third_party_libraries'][key]['url'][type][type2] = url2.gsub('{{version}}', site.config['third_party_libraries'][key]['version'])
            end
          end
        else
          # replace {{version}} with the version number if it exists
          if url.include?('{{version}}')
            site.config['third_party_libraries'][key]['url'][type] = url.gsub('{{version}}', site.config['third_party_libraries'][key]['version'])
          end
        end
      end
    end
  end

  # download 3rd party libraries if required
  if site.config['third_party_libraries']['download']
    site.config['third_party_libraries'].each do |key, value|
      if key != 'download'
        value['url'].each do |type, url|
          # check if url is a dictionary
          if url.is_a?(Hash)
            url.each do |type2, url2|
              # get the file name from the url
              file_name = url2.split('/').last.split('?').first
              # download the file and change the url to the local file
              dest = File.join(site.source, 'assets', 'libs', key, file_name)
              download_file(url2, dest)
              # change the url to the local file, considering baseurl
              site.config['third_party_libraries'][key]['url'][type][type2] = local_asset_path(site.config, key, file_name)
            end

          else
            if type == 'fonts'
              # get the file name from the url
              file_name = url.split('/').last.split('?').first

              if file_name.end_with?('css')
                # if the file is a css file, download the css file, the fonts from it, and change information on the css file
                file_name = download_fonts_from_css(site.config, url, File.join(site.source, 'assets', 'libs', key), key, font_file_types)
                # change the url to the local file, considering baseurl
                site.config['third_party_libraries'][key]['url'][type] = local_asset_path(site.config, key, file_name)
              else
                # download the font files and change the url to the local file
                download_fonts(url, File.join(site.source, 'assets', 'libs', key, site.config['third_party_libraries'][key]['local'][type]), font_file_types)
              end

            elsif type == 'images'
              # download the font files and change the url to the local file
              download_images(url, File.join(site.source, 'assets', 'libs', key, site.config['third_party_libraries'][key]['local'][type]), image_file_types)

            else
              # get the file name from the url
              file_name = url.split('/').last.split('?').first
              # download the file and change the url to the local file
              dest = File.join(site.source, 'assets', 'libs', key, file_name)
              download_file(url, dest)
              if key == 'pseudocode' && type == 'css'
                replace_file_text(
                  dest,
                  {
                    '@import url(https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.7/katex.min.css);' =>
                      "@import url(#{local_asset_path(site.config, 'katex', 'katex.min.css')});"
                  }
                )
              end
              # change the url to the local file, considering baseurl
              site.config['third_party_libraries'][key]['url'][type] = local_asset_path(site.config, key, file_name)
            end
          end
        end
      end
    end
  end
end
