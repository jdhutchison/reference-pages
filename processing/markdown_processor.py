import os
import shutil

###############################################################################
###############################################################################
###                                                                         ###
###                   MARKDOWN PROCESSING SCRIPT                            ###
###                                                                         ###
### Converts Markdown exported from Joplin into Makrdown that Hugo can      ###
### generate HTML from.                                                     ###
###                                                                         ###
###############################################################################
###############################################################################

# The root directory for the markdown source
SRC_ROOT='/tmp/General'

# The root directory for Hugo markdown
HUGO_CONTENT_ROOT='/data/code/reference-pages/pages/content'

# The prefix for the paths in the URLs 
ONLINE_PATH='/ref/'


def kebab_case_file_path(original_path):
    """
    Converts a filename (or any string really) into a kebab-case file name. Also removes underscores.

    @param original_path (str) A relative path to convert.
    @return str The converted path.
    """
    return original_path.lower().replace(' ', '-').replace('_', '')


def add_front_matter(contents, weight):
    """
    Processes the contents of a markdown file by:
    a) Adding metdata data in YAML front matter format.
    b) Removing a duplicate top level title if it exists, as Hugo will generate its own. s

    @param contents (List[str]) The original contents of the file to be modified. 
    @param weight (int) The page weight 
    @return List[str] the modified markdown, one line per list entry. This list is not the same as the
    contents parameter. 
    """
    new_contents = ['---']
    new_contents.append('title: ' + contents[0])
    new_contents.append('weight: ' + str(weight))
    new_contents.append('---')
    
    idx = 1
    while idx < len(contents):
        if contents[idx].startswith('==='):
            del new_contents[-1] # Remove the duplicated title. 
            idx += 2 # Skip the blank line under the heading sig
        else: 
            new_contents.append(contents[idx])
            idx += 1

    return new_contents

def process_file(relpath, weight=1):
    """
    Processes a markdown file by adding metadata, deleting the original file and writing the modified contents to
    Hugo's content directory. 
 
    
    @param relpath (str) the relative (to the makdown root) path of this file. 
    @param weight (int) the weight (or ranking in listings) of this page within its section. 
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

def generate_index_list_section(entries, web_path, make_bold=False):
    """
    Outputs a markdown list of web links from a list of directory entries. 

    @param entries (List[str]) the entries for this list. 
    @param web_path (str) the prefix for the path of an entry on the actual site. 
    @param make_bold (bool) if the entry name should be displayed in bold. Defaults to false. 

    @return List[str] the markdown for the list of entries. 
    """
    lines_of_list = []
    
    for entry in entries:
        title = entry.replace('_', '').replace('.md', '')
        url = os.path.join(web_path, kebab_case_file_path(title))
        line_fmt = '- [**%s**](%s)' if make_bold else '- [%s](%s)'
        lines_of_list.append(line_fmt % (title, url)) 

    return lines_of_list

def generate_index(relpath, directories, files):
    """
    For a given directory generates the markdown that goes into that directory's _index.md file. 

    @param relpath (str) the relative (to the makdown root) path of this directory.
    @param directories (List[str]) the names of directories within this section. 
    @param files (List[str]) the names of files within this directory. 
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
    content.append('type: section')
    content.append('---')
    content.append('')

    if len(directories):
        content += generate_index_list_section(directories, web_path, True)
        content.append('')

    if len(files):
          content += generate_index_list_section(files, web_path) 
 
    with open(hugo_path + '/_index.md', 'w') as out:
        for line in content:
            print(line, file=out)

def sort_entries_in_directory(abs_path):
    """
    Reads entries in a directory, sorting them into sub-directories and files. These sets are
    then sorted alphabetically. 

    @param abs_path The absolute path of the directory to sort the entries for. 

    @return Tuple(List[str], List[str]) the list of directories and files in a tuple.  
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
    Processes a directory of markdown files into Hugo ready markdown files. 

    @param relpath (str) the relative (to the makdown root) path of this file. Defaults to empty, which is the root directory. 
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
    # Delete the existing content
    shutil.rmtree(HUGO_CONTENT_ROOT)
 
    # Walk tree - process root directory
    process_directory()
