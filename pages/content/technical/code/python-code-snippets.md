---
title: Python code snippets
weight: 1
---

Dates and times
---------------

### Formatting a date or time

```python
>>> import datetime
>>> d = datetime.datetime.now()
>>> d.strftime('%Y-%m-%d')
'2020-09-02'
>>> datetime.datetime.strptime('02/09/2020', '%d/%m/%Y')
datetime.datetime(2020, 9, 2, 0, 0)
```

See the [format codes documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) for complete list of formatting codes.

Files
-----

### Making a zip file
[Docs](https://docs.python.org/3/library/shutil.html#shutil.make_archive)

```python
import shutil

shutil.make_archive('<file base path>', 'zip', '<root path for files to zip up>', '<root path>'[, '<base_path>'])
```

_root path_: The path that the files start getting zipped up from. Typically gets chdired into.

_base path_: Inside of _root path_ where the files are zipped up in. Typically use '.'.

### Retain newest n files, delete the rest
```python
import os

def keep_n_newest_files(path, num_to_keep):
# Finds all files in the path/dir
files = [f for f in os.scandir(path) if f.is_file()]

# Sorts oldest to newest
files.sort(key = lambda f: f.stat().st_ctime)

for f in files[:-num_to_keep]:
os.remove(f.path)
```

### Read file into list of lines
```python
with open(filename) as f:
content = f.readlines()

# Strip and trailing whitespace
content = [l.strip() for l in content]
```

