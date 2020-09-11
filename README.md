The Reference Pages project
===========================

Static generation from markdown for reference pages for my personal site. There's some Python processing scripts for converting markdown exported from Joplin into somethig more useful for Hugo. And then theres the hugo configuration, including the most recent converted markdown.

Structure
---------

The project has two folders:

**processing**: Python scripts to convert exported markdown and bash scripts to run on the client and server. 

**pages**: Configuration and content for Hugo to run with. 
.

To Run
------

On the client, to extract from Joplin and process the markdown:
```
/<path to project>/processing/export_and_upload.sh
```

On the server running the pages:
```
/<path to project>/processing/download_and_generate.sh
```


To Do
-----
This project is stable for now but functionality to do in the future:
- Extract bookmarks from Firefox
- Handle images. 
