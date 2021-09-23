# A very simple script to generate a blog html page using jinja2
import jinja2

outfile = 'blog.html'

titles = ['1st title', '2nd title', '3rd title']
texts = ['This is an exaple of a 1st post.', 'And this is a second post.', 'Also a 3rd one to fullfils the rule of 3s.']

subs = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template('template.html').render(titles=titles, text=texts)

with open(outfile, 'w') as f: f.write(subs)
