#!/bin/bash

###############################################################################
###############################################################################
###                                                                         ###
###               MARKDOWN DOWNLOAD AND GENERATE SCRIPT                     ###
###                                                                         ###
### Pulls repository from Git and generates static content. To be run on    ###
### the server. Hugp and Git must be installed for this to run.             ###
### This script has no command line params.                                 ###
###############################################################################
###############################################################################


WWW_FOLDER='/var/www/hutch.id.au/ref'
HUGO_ROOT='/tmp'

# Tidyup - remove old copies
rm -r $WWW_FOLDER/*
cd $HUGO_ROOT
git clone https://github.com/jdhutchison/reference-pages.git
cd reference-pages/pages
/usr/local/bin/hugo -D --theme solar-theme-hugo -d $WWW_FOLDER
chown -R www-data:www-data $WWW_FOLDER

# Can remove repo
rm -r $HUGO_ROOT/reference-pages

