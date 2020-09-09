import os
import shutil

SRC_ROOT='/tmp/General'

HUGO_CONTENT_ROOT='/data/code/reference-pages/pages/content'

ONLINE_PATH='/ref/'

def process_directory(relpath):
    pass

def kebab_case_file_path(original_path):
    """
    Converts a filename (or any string really) into a kebab-case file name. 
    """
    return original_path.lower().replace(' ', '-').replace('_', '')


def add_front_matter(contents, weight):
    """
    """
    new_contents = ['---']
    new_contents.append('title: ' + contents[0])
    new_contents.append('weight: ' + str(weight))
    new_contents.append('---')
    
    idx = 1
    while idx < len(contents):
        if contents[idx].startswith('==='):
            del new_contents[-1]
            idx += 2 # Skip the blank line under the heading sig
        else: 
            new_contents.append(contents[idx])
            idx += 1

    return new_contents

def process_file(relpath, weight=1):
    """
    """
    # Read file
    with open(os.path.join(SRC_ROOT, relpath)) as filein:
        content = filein.readlines()
    
    content = [l.strip() for l in content]

    # Generate header, process lines
    content = add_front_matter(content, weight)

    # Determine new name
    newpath = os.path.join(HUGO_CONTENT_ROOT, kebab_case_file_path(relpath))

    # Write out the new file
    with open(newpath, 'w') as out:
        for line in content:
            print(line, file=out)

    # Delete original file
    os.remove(os.path.join(SRC_ROOT, relpath))

def generate_index_list_section(heading, entries, web_path, make_bold=False):
    """
    """
    lines_of_list = ['## ' + heading, '']
    
    for entry in entries:
        title = entry.replace('_', '').replace('.md', '')
        url = os.path.join(web_path, kebab_case_file_path(title))
        line_fmt = '- [**%s**](%s)' if make_bold else '- [%s](%s)'
        lines_of_list.append(line_fmt % (title, url)) 

    return lines_of_list

def generate_index(relpath, directories, files):
    """
    """
    hugo_rel_path = kebab_case_file_path(relpath)

    hugo_path = os.path.join(HUGO_CONTENT_ROOT, hugo_rel_path)
    web_path = os.path.join(ONLINE_PATH, hugo_rel_path)
    title = relpath.split('/')[-1]
    content = []
    content.append('---')
    if len(title):
        content.append('title: ' + title)
    content.append('weight: 0')
    content.append('type: page')
    content.append('---')
    content.append('')

    if len(directories):
        content += generate_index_list_section('Sub-sections', directories, hugo_path, True)
        content.append('')

    if len(files):
          content += generate_index_list_section('Pages', files, web_path) 
 
    with open(hugo_path + '/_index.md', 'w') as out:
        for line in content:
            print(line, file=out)

def sort_entries_in_directory(abs_path):
    """
    """
    directories = []
    files = []

    # Read contents - Sort into directories and files
    for node in os.scandir(abs_path):
        if node.is_dir():
            directories.append(node.name)
        else:
            files.append(node.name)

    directories.sort()
    files.sort()
    return (directories, files)

def process_directory(relpath=''):
    """
    """
    abs_path = os.path.join(SRC_ROOT, relpath)
    os.mkdir(os.path.join(HUGO_CONTENT_ROOT, kebab_case_file_path(relpath)))

    # Read contents - Sort into directories and files
    directories, files = sort_entries_in_directory(abs_path)   

    # Recursively process directories
    for d in directories:
        process_directory(os.path.join(relpath, d))

    # Process files
    weight = len(directories) + 1
    for f in files:
        process_file(os.path.join(relpath, f), weight)

    # Generate index file
    generate_index(relpath, directories, files)
    shutil.rmtree(abs_path)

if __name__ == '__main__':
    # Extract?

    # Delete the existing content
    shutil.rmtree(HUGO_CONTENT_ROOT)
 
    # Walk tree - process root directory
    process_directory()
