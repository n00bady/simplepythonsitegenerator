# About
A simple script to convert a bunch of markdown files to html and then make an index page linking to them.
I use it to easily create posts for my blog in my own site.
# Usage
Just call the script and give the template for the post as the first argument and the template for the index page
as a second argument.
```
spsg.py template.html index_template.html
```
All posts must be in markdown format in the ./\_posts/ directory all output will be at ./blog/
if the script encounter a non .md file in the ./\_posts/ folder then a warning will be displayed and the file
will be skipped.  
The markdown files must be named with in the form of `year-month-day-title.md` to be properly ordered from
newest to oldest in the index page.

My template html files for my own site are included for testing.
