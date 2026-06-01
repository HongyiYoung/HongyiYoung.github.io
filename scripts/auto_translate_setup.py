import os
import shutil
import re

# Logic:
# 1. Scan specific directories (_pages, _projects, _news)
# 2. Find .md files that do not end with _zh.md or are not in language subdirs (like /ch/)
# 3. Check if a corresponding Chinese version exists.
#    - For _pages/foo.md, check _pages/foo_zh.md or ch/foo.md (depending on your structure strategy)
#    - For _projects/foo.md, check _projects/foo_zh.md
#    - For _news/foo.md, check _news/foo_zh.md
# 4. If not exists, create it.
# 5. Modify front matter to set 'lang: zh'.

DIRS_TO_SCAN = [
    {
        'path': '_projects', 
        'suffix': '_zh.md' 
    },
    {
        'path': '_news', 
        'suffix': '_zh.md'
    },
]

# For _pages, user seems to use /ch/ subdirectory mostly, but for news/projects it's suffixes.
# We will focus on the suffixed ones as per user complaint.

def sync_directories():
    base_dir = os.getcwd()
    
    for item in DIRS_TO_SCAN:
        search_dir = os.path.join(base_dir, item['path'])
        if not os.path.exists(search_dir):
            continue
            
        print(f"Scanning {item['path']}...")
        
        for filename in os.listdir(search_dir):
            if not filename.endswith('.md'):
                continue
            
            # Skip existing chinese files
            if filename.endswith(item['suffix']):
                continue
                
            # Construct expected chinese filename
            name_root = filename[:-3] # remove .md
            zh_filename = name_root + item['suffix']
            zh_filepath = os.path.join(search_dir, zh_filename)
            
            if os.path.exists(zh_filepath):
                print(f"  [Skip] {zh_filename} already exists.")
                continue
                
            # Create new file
            src_path = os.path.join(search_dir, filename)
            
            try:
                with open(src_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Parse Front Matter
                if content.startswith('---'):
                    parts = content.split('---', 2)
                    if len(parts) >= 3:
                        front_matter = parts[1]
                        body = parts[2]
                        
                        # Add lang: zh
                        if 'lang: zh' not in front_matter:
                            front_matter = front_matter + "lang: zh\n"
                        
                        # Optional: Mark title as (ZH) or similar? 
                        # For now, let's keep it clean so user only translates content
                        
                        new_content = '---' + front_matter + '---\n\n> ⚠️ **Draft: This content needs to be translated to Chinese.**\n\n' + body
                        
                        # Write to new file
                        with open(zh_filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        print(f"  [Create] {zh_filename} created.")
                    else:
                        print(f"  [Error] {filename} seems to have invalid front matter.")
                else:
                    print(f"  [Skip] {filename} no front matter found.")

            except Exception as e:
                print(f"  [Error] Failed to process {filename}: {e}")

if __name__ == "__main__":
    sync_directories()
    print("Sync completed. You can now manually translate the content in the newly created _zh.md files.")
