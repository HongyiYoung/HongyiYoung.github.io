import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def require(condition, message):
    if not condition:
        raise AssertionError(message)


layout = read("_layouts/about.liquid")
head = read("_includes/head.liquid")
header = read("_includes/header.liquid")
main_scss = read("assets/css/main.scss")
custom = read("_sass/_custom.scss")
inline_custom = read("_includes/custom_styles.liquid")
base_styles = read("_sass/_base.scss")
cv_styles = read("_sass/_cv.scss")
theme_styles = read("_sass/_themes.scss")
cache_bust_plugin = read("_plugins/cache-bust.rb")
download_third_party_plugin = read("_plugins/download-3rd-party.rb")
social_include = read("_includes/social.liquid")
news_include = read("_includes/news.liquid")
bib_layout = read("_layouts/bib.liquid")
scripts_include = read("_includes/scripts.liquid")
distill_scripts_include = read("_includes/distill_scripts.liquid")
distill_template_js = read("assets/js/distillpub/template.v2.js")
distill_transforms_js = read("assets/js/distillpub/transforms.v2.js")
footer_include = read("_includes/footer.liquid")
resume_skills_include = read("_includes/resume/skills.liquid")
resume_interests_include = read("_includes/resume/interests.liquid")
resume_languages_include = read("_includes/resume/languages.liquid")
about = read("_pages/about.md")
zh_about = read("ch/index.md")
resume_en = read("assets/json/resume.json")
resume_zh = read("assets/json/resume_zh.json")
legacy_cv = read("_data/cv.yml")
resume_tex = read("resume_content.tex")
electronic_project = read("_projects/electronic_design_2025.md")
electronic_project_zh = read("_projects/electronic_design_2025_zh.md")
admin_data = read("admin_data.js")
admin_page = read("admin.html")
site_config = read("_config.yml")
coauthors = read("_data/coauthors.yml")
news_2024_honors = read("_news/2024honors.md")
news_2025_honors = read("_news/2025honors.md")
deploy_workflow = read(".github/workflows/deploy.yml")
release_script = read("release.sh")
gitignore = read(".gitignore")
resume_en_data = json.loads(resume_en)
resume_zh_data = json.loads(resume_zh)
language_toggle_block = base_styles.split("\n\n.language-toggle {\n", 1)[1].split("\n}", 1)[0]

require("profile_onerror" in layout, "profile image should define a controlled fallback on load failure")
require("cache_bust=true" not in layout, "profile image should not force cache-busted URLs")
require('loading="eager"' in layout, "profile image should keep eager loading")
require("fetchpriority=\"high\"" in layout, "profile image should request high fetch priority")
require("path=profile_image_path" in layout, "profile image should use the existing profile image path")
require('width="800" height="1120"' in layout, "profile image should declare the real image dimensions")
require('figure_class="profile-image-figure"' in layout, "profile image should have a scoped figure class")
require("profile-image-fallback" in layout, "profile image should switch to the fallback presentation on error")
require(".profile-image-figure.profile-image-fallback" in custom, "profile image fallback styles should be defined")
require("prof_pic-480.webp" not in layout and "prof_pic-480.webp" not in head, "profile image should not preload a missing WebP asset")
require("prof_pic.jpg" in head and "image/jpeg" in head, "profile image preload should target the existing JPEG asset")
require(
    "assets/fonts/tabler-icons.woff2" in head
    and 'rel="preload"' in head
    and 'as="font"' in head
    and "font/woff2" in head,
    "Tabler icon font should be preloaded from local site assets",
)
require(
    "download: true # download these libraries during build and serve them from /assets/libs/" in site_config,
    "third-party libraries should be downloaded during build and served locally",
)
require(
    "altmetric: false" in site_config and "dimensions: false" in site_config,
    "unused dynamic publication badge scripts should stay disabled",
)
require(
    "la51:" in site_config
    and "https://sdk.51.la/js-sdk-pro.min.js" in site_config
    and "{{ site.third_party_libraries.la51.url.js }}" in scripts_include
    and "{{ site.third_party_libraries.la51.url.js }}" in distill_scripts_include,
    "51.LA SDK should be routed through third-party library local download config",
)
require(
    "tikzjax:" in site_config
    and "tikzjax_fonts:" in site_config
    and "{{ site.third_party_libraries.tikzjax.url.js }}" in scripts_include
    and "{{ site.third_party_libraries.tikzjax.url.js }}" in distill_scripts_include
    and "{{ site.third_party_libraries.tikzjax_fonts.url.fonts }}" in head,
    "TikZJax assets should be routed through third-party library local download config",
)
require(
    "webcomponentsjs:" in site_config
    and "/assets/libs/webcomponentsjs/webcomponents-loader.js" in distill_transforms_js
    and "https://cdnjs.cloudflare.com/ajax/libs/webcomponentsjs/" not in distill_transforms_js,
    "Distill webcomponents loader should use the local third-party library copy",
)
require(
    "katex:" in site_config
    and "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.7/katex.min.css" in site_config
    and "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.7/katex.min.js" in site_config
    and "/assets/libs/katex/katex.min.css" in distill_template_js
    and "/assets/libs/katex/katex.min.js" in distill_template_js
    and "/assets/libs/katex/katex.min.css" in distill_transforms_js
    and "https://distill.pub/third-party/katex/" not in distill_template_js
    and "https://distill.pub/third-party/katex/" not in distill_transforms_js,
    "Distill KaTeX runtime assets should use the local third-party library copy",
)
require(
    "def local_asset_path" in download_third_party_plugin
    and "source_url = nil" in download_third_party_plugin
    and "URI.join(source_url || '', url).to_s" in download_third_party_plugin,
    "third-party downloader should resolve relative URLs in CSS font files against the stylesheet URL",
)
require(
    "Tempfile" in download_third_party_plugin
    and "downloadable_values" in download_third_party_plugin
    and "Skipping unavailable font source" in download_third_party_plugin,
    "third-party downloader should handle multi-source CSS fonts and skip unavailable fallback formats",
)
require(
    "https://tikzjax.com/v1/" not in head
    and "https://tikzjax.com/v1/" not in scripts_include
    and "https://tikzjax.com/v1/" not in distill_scripts_include
    and "https://sdk.51.la/js-sdk-pro.min.js" not in scripts_include
    and "https://sdk.51.la/js-sdk-pro.min.js" not in distill_scripts_include,
    "head and script includes should not hard-code localizable external library URLs",
)
require(
    '"tabler-icons/tabler-icons.scss"' in main_scss
    and "tabler-icons-filled.scss" not in main_scss
    and "tabler-icons-outline.scss" not in main_scss,
    "Tabler icons should use the complete local font without duplicate filled/outline imports",
)

require("ZhiMangXingNameSubset" in custom, "custom stylesheet should define the expressive name font subset")
require("ZhiMangXing-name-subset.woff2" in custom, "custom stylesheet should load the expressive WOFF2 subset")
require("font-display: swap" in custom, "name font should not block text rendering")
require("name-calligraphy" in layout, "layout should use the subset-backed name style")
require("font-family: 'ZhiMangXingNameSubset'" in custom, "name style should use the expressive subset font family")
require("language-toggle" in header, "header should expose an explicit language toggle")
require("Change language" in header, "language toggle should have an English title")
require("切换语言" in header, "language toggle should expose a Chinese label")
require(
    'class="toggle-container search-toggle-container"' in header,
    "search toggle should use the same flex container as theme/language toggles",
)
require(
    "#light-toggle,\n#search-toggle,\n.language-toggle" in base_styles,
    "language toggle should share the same nav action sizing as search/theme buttons",
)
require(
    ".search-toggle-container" in base_styles,
    "search toggle container should be explicitly centered with the other nav actions",
)
require(
    "#search-toggle .nav-link {\n  color: inherit;" in base_styles
    and "#search-toggle i {\n  color: inherit;" in base_styles,
    "search toggle internals should inherit theme-aware button color",
)
require(
    ".language-toggle {\n  font-size" in base_styles and "border:" not in language_toggle_block,
    "language toggle should not render with an outer border",
)
require(
    "border-radius:" not in language_toggle_block,
    "language toggle should not render as a pill/circle",
)
require(
    "@media (max-width: 575.98px)" in base_styles
    and "#navbarNav .navbar-nav" in base_styles
    and ".toggle-container" in base_styles,
    "mobile navbar should explicitly center collapsed nav actions",
)
require(
    "#light-toggle-system,\n#light-toggle-dark,\n#light-toggle-light" in theme_styles
    and "padding-left: 10px" not in theme_styles
    and "padding-top: 12px" not in theme_styles,
    "theme icons should be centered by the button layout, not hard-coded padding",
)
require(
    ".contact-icons" in base_styles
    and ".cv-icon-svg" in base_styles
    and "<style>" not in social_include,
    "CV icon sizing should live in shared SCSS instead of inline include styles",
)
require(
    "@media (max-width: 575.98px)" in base_styles
    and ".contact-icons" in base_styles
    and ".cv-icon-svg" in base_styles,
    "mobile contact icons should keep CV and email visually matched",
)
require(
    "background: rgba(var(--global-theme-color-rgb)" not in base_styles
    and "border-radius: 50%" not in base_styles
    and "font-size: 1.3em" not in base_styles,
    "legacy mobile contact icon styling should not override the shared CV/email sizing",
)
require(
    "transform: translateY(0.08em)" in custom and "vertical-align: baseline" in custom,
    "name calligraphy should be baseline-adjusted for the current font",
)
for styles in (custom, inline_custom):
    require("linear-gradient(135deg" not in styles, "stat cards should avoid bright fixed gradients")
    require("var(--stat-card-bg)" in styles, "stat cards should use theme-aware custom properties")
    require("html[data-theme=\"dark\"]" in styles, "stat cards should define a dark-theme palette")
    require("container-type: inline-size" in styles, "stat cards should size text against their own card width")
    require("overflow: hidden" in styles, "stat cards should clip accidental overflow inside the card")
    require("stat-value-wide" in styles, "stat cards should define a compact long-value variant")
    require(
        "font-size: 1.25rem" in styles and "clamp(1.2rem, 12cqw, 1.62rem)" in styles,
        "long stat values should have a small fallback and card-relative responsive font size",
    )

for text in (about, zh_about):
    require(
        'class="stat-value stat-value-wide">4.10/5.00</div>' in text,
        "GPA stat should use the compact long-value class to prevent card overflow",
    )
    require("Merit Student" in text or "三好学生" in text, "homepage should mention merit student")
    require(
        "Outstanding Student Cadre" in text or "优秀学生干部" in text,
        "homepage should mention outstanding student cadre",
    )

def has_award(data, title, date):
    return any(award.get("title") == title and award.get("date") == date for award in data.get("awards", []))


require(
    has_award(resume_en_data, "Merit Student of Southwest University", "2024-10"),
    "English resume should show 2024-10 merit student award without a day",
)
require(
    has_award(resume_en_data, "Outstanding Student Cadre of Southwest University", "2024-10"),
    "English resume should show 2024-10 cadre award without a day",
)
require(
    has_award(resume_zh_data, "西南大学三好学生", "2024-10"),
    "Chinese resume should show 2024-10 merit student award without a day",
)
require(
    has_award(resume_zh_data, "西南大学优秀学生干部", "2024-10"),
    "Chinese resume should show 2024-10 cadre award without a day",
)

for data in (resume_en_data, resume_zh_data):
    patent_awards = [
        award
        for award in data.get("awards", [])
        if award.get("title") in {"National Invention Patent", "国家发明专利"}
    ]
    require(patent_awards, "resume should include the invention patent award")
    require(
        all(award.get("url") == "https://cponline.cnipa.gov.cn/" for award in patent_awards),
        "invention patent should link to CNIPA online portal",
    )

require("省级" not in resume_zh, "Chinese resume should use 省部级 instead of 省级")
require("省部级" in resume_zh, "Chinese resume should mention 省部级 awards")

require(
    "experience in Multimodal Large Models, Computer Vision, and Embedded Development" in resume_en_data["basics"]["summary"],
    "English resume about summary should mention multimodal, computer vision, and embedded development experience",
)
require(
    "有多模态大模型、计算机视觉、嵌入式等开发经验" in resume_zh_data["basics"]["summary"],
    "Chinese resume about summary should mention multimodal, computer vision, and embedded development experience",
)
require(
    "experience in Multimodal Large Models, Computer Vision, and Embedded Development" in about,
    "English homepage about should mention multimodal, computer vision, and embedded development experience",
)
require(
    "有多模态大模型、计算机视觉、嵌入式等开发经验" in zh_about,
    "Chinese homepage about should mention multimodal, computer vision, and embedded development experience",
)

require(
    [skill["name"] for skill in resume_en_data["skills"]] == ["Programming Languages", "Artificial Intelligence"],
    "English resume skills should keep only programming languages and artificial intelligence",
)
require(
    [skill["name"] for skill in resume_zh_data["skills"]] == ["编程语言", "人工智能"],
    "Chinese resume skills should keep only programming languages and artificial intelligence",
)
require(
    resume_en_data["skills"][1]["keywords"] == [
        "MLLM",
        "DL",
        "CV",
        "NLP",
    ],
    "English AI skills should use compact MLLM/DL/CV/NLP labels",
)
require(
    resume_zh_data["skills"][1]["keywords"] == ["MLLM", "DL", "CV", "NLP"],
    "Chinese AI skills should use compact MLLM/DL/CV/NLP labels",
)
require("resume-skill-groups" in resume_skills_include, "skills include should expose a CV-specific style hook")
require(
    "resume-keyword-with-level" in resume_skills_include
    and "resume-keyword-name" in resume_skills_include
    and "resume-keyword-level" in resume_skills_include,
    "skills include should split programming-language names and proficiency levels onto separate lines",
)
require("resume-interest-groups" in resume_interests_include, "interests include should expose a CV-specific style hook")
require(".resume-skill-groups" in cv_styles, "CV stylesheet should style the compact skills section")
require("grid-template-columns: repeat(2, minmax(0, 1fr))" in cv_styles, "CV skills should render keywords as an equal 2x2 grid")
require(
    ".resume-keyword-with-level" in cv_styles
    and ".resume-keyword-level" in cv_styles,
    "CV stylesheet should style split programming-language proficiency labels",
)
require(
    "Visited 20+ provinces in China" in resume_en
    and "Visited 20+ provinces and regions in China" not in resume_en
    and "Visited 20+ provinces and regions in China" not in legacy_cv,
    "English travel interest should say Visited 20+ provinces in China",
)
require(
    "游历中国20+省份" in resume_zh and "省份及地区" not in resume_zh,
    "Chinese travel interest should sync the 20+ provinces wording",
)
require(".resume-interest-groups" in cv_styles, "CV stylesheet should style the compact interests section")
require(
    "resume-interest-card" in resume_interests_include,
    "interests include should expose dedicated card hooks for cleaner layout",
)
require(
    "div.resume-interest-groups {\n  display: grid;" in cv_styles
    and "grid-template-columns: repeat(3, minmax(0, 1fr))" in cv_styles,
    "CV interests should use a stable equal three-column grid on desktop",
)
require(
    ".resume-interest-groups .resume-keyword-list" in cv_styles
    and "grid-template-columns: 1fr" in cv_styles,
    "CV interest keywords should use uniform full-width rows",
)
require(
    "resume-language-groups" in resume_languages_include
    and "resume-language-card" in resume_languages_include,
    "languages include should expose dedicated hooks for compact layout",
)
require(
    "div.resume-language-groups {\n  display: grid;" in cv_styles
    and "grid-template-columns: repeat(3, minmax(0, 1fr))" in cv_styles,
    "CV languages should use a compact equal three-column grid",
)
require("max-width: 34rem" in cv_styles, "CV languages should not stretch across the full section width")
require(
    "directory: '_sass'" in cache_bust_plugin,
    "CSS cache busting should hash the real _sass directory instead of an empty path",
)

featured_news = [
    "2025Scholarship",
    "2025honors",
    "Electronic",
    "finalist",
    "2024Scholarship",
]
for slug in featured_news:
    require(f"featured: true" in read(f"_news/{slug}.md"), f"English featured news missing: {slug}")
    require(f"featured: true" in read(f"_news/{slug}_zh.md"), f"Chinese featured news missing: {slug}")

for slug in ["patent", "lanqiao", "cumcm", "2024honors"]:
    require(f"featured: true" not in read(f"_news/{slug}.md"), f"English non-homepage news should not be featured: {slug}")
    require(f"featured: true" not in read(f"_news/{slug}_zh.md"), f"Chinese non-homepage news should not be featured: {slug}")

require(
    "where: 'featured', true" in news_include and "news_featured" in news_include,
    "homepage news include should prefer featured items when limited",
)
require("省级一等奖" not in read("_news/Electronic_zh.md"), "Chinese electronic news should use 省部级一等奖")
require("省部级一等奖" in read("_news/Electronic_zh.md"), "Chinese electronic news should mention 省部级一等奖")
require("Provincial Level" in read("_news/Electronic.md"), "English electronic news should use Provincial Level")
for path, text in {
    "ch/index.md": zh_about,
    "assets/json/resume_zh.json": resume_zh,
    "resume_content.tex": resume_tex,
    "_projects/electronic_design_2025_zh.md": electronic_project_zh,
    "admin_data.js": admin_data,
}.items():
    require("省级一等奖" not in text, f"{path} should use 省部级一等奖 instead of 省级一等奖")
    require("省级二等奖" not in text, f"{path} should use 省部级二等奖 instead of 省级二等奖")
for path, text in {
    "_pages/about.md": about,
    "assets/json/resume.json": resume_en,
    "_data/cv.yml": legacy_cv,
    "_projects/electronic_design_2025.md": electronic_project,
    "_news/Electronic.md": read("_news/Electronic.md"),
    "_news/cumcm.md": read("_news/cumcm.md"),
    "admin_data.js": admin_data,
}.items():
    require("Provincial/Ministerial" not in text, f"{path} should use Provincial in English")
require("Provincial 1st Prize" in about, "English homepage awards should use Provincial 1st Prize")
require("Provincial First Prize" in electronic_project, "English project page should use Provincial First Prize")
require("省部级一等奖" in electronic_project_zh, "Chinese project page should use 省部级一等奖")
require("省部级一等奖" in resume_tex and "省部级二等奖" in resume_tex, "TeX resume should use 省部级 wording")
require("enable_51la_analytics: true" in site_config, "51.LA analytics should be enabled in site config")
require(
    'la51_analytics_id: "3OTnyWhHyoe0kxf2"' in site_config
    and 'la51_analytics_ck: "3OTnyWhHyoe0kxf2"' in site_config,
    "51.LA v6 app id and ck should be configured in _config.yml",
)
require(
    "site.la51_analytics_id" in scripts_include
    and "site.la51_analytics_ck" in scripts_include
    and "site.la51_analytics_id" in distill_scripts_include
    and "site.la51_analytics_ck" in distill_scripts_include
    and "{{ site.third_party_libraries.la51.url.js }}" in scripts_include
    and "{{ site.third_party_libraries.la51.url.js }}" in distill_scripts_include,
    "51.LA script includes should use configured v6 credentials and locally routed SDK",
)
require(
    "site.data.build.last_updated" in footer_include and "'now'" not in footer_include,
    "footer last updated date should come from deploy-generated build data instead of Liquid now",
)
require(
    "_data/build.yml" in deploy_workflow and "Asia/Shanghai" in deploy_workflow,
    "deploy workflow should generate a timezone-aware build date for the footer",
)
require(
    "_data/build.yml" in release_script and "Asia/Shanghai" in release_script,
    "local release script should generate the same timezone-aware build date for the footer",
)
require("_data/build.yml" in gitignore, "generated build date data should stay out of source commits")
for honors_news in (news_2024_honors, news_2025_honors):
    require(
        "[Southwest University](https://swu.edu.cn/){:target=\"_blank\"}" in honors_news,
        "English honors news should link Southwest University to the official website",
    )
for admin_text in (admin_data, admin_page):
    require(
        "https://swu.edu.cn/" in admin_text
        and "Honored as **Merit Student** at Southwest University!" not in admin_text
        and "Outstanding Student Cadre** at Southwest University!" not in admin_text,
        "admin news defaults should keep Southwest University linked",
    )
require(
    "max_author_limit: 3" not in site_config,
    "publication authors should not be collapsed behind a maximum author limit",
)
require(
    "class=\"more-authors\"" not in bib_layout and "more_authors" not in bib_layout,
    "publication template should render all authors directly instead of a more-authors expander",
)
require(
    ".author {\n        a {\n          color: var(--global-theme-color);\n          border-bottom: none;\n          text-decoration: none;" in base_styles
    and "&:hover {\n            color: var(--global-theme-color);\n            border-bottom: none;\n            text-decoration: none;" in base_styles,
    "linked publication authors should use color only, without dashed or hover underlines",
)
require(
    "https://bingyaohuang.github.io/" in coauthors,
    "Bingyao Huang should link to the configured personal homepage",
)
require(
    "https://haibinling.github.io/" in coauthors,
    "Haibin Ling should link to the configured personal homepage",
)
require("profile-info-card" in about and "profile-info-card" in zh_about, "profile info should use the compact card markup")
require(".profile-info-card" in custom and ".profile-info-item" in custom, "profile info card styles should be defined")
require(
    ".profile-info-card" in inline_custom and ".profile-info-item" in inline_custom,
    "inlined custom styles should style the profile info card loaded by the page",
)

for asset in ("assets/img/prof_pic.jpg", "assets/fonts/ZhiMangXing-name-subset.woff2"):
    require((ROOT / asset).exists(), f"missing optimized asset: {asset}")

if (ROOT / "_site").exists():
    require(
        (ROOT / "_site/assets/img/prof_pic.jpg").exists(),
        "built site should contain the profile image asset",
    )

print("Homepage asset checks passed.")
