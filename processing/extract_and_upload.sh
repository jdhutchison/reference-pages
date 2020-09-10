#!/bin/bash

###############################################################################
###############################################################################
###                                                                         ###
###                 MARKDOWN EXTRACT AND UPLOAD SCRIPT                      ###
###                                                                         ###
### Extracts markdown from Joplin, calls the processing script and then     ###
### uploads to Git. THis script is to be run locally.                       ###
##  This script has no command line params.                                 ###
###############################################################################
###############################################################################

REF_PAGES_HOME='/data/code/reference-pages'
DATE=$(date +%F)

rm -rf /tmp/General
joplin export /tmp --notebook=General --format=md
python3 $REF_PAGES_HOME/processing/markdown_processor.py
cd $REF_PAGES_HOME/pages/content
git add *
git commit -m "Automatic upload on $DATE"
git push

