# A very simple script to generate a blog html page using jinja2
import jinja2
import markdown

outfile = 'blog.html'
# TODO: Add taking input/output files as cli arguments
with open('test.md', 'r') as md:
    m = markdown.Markdown(extensions=['markdown.extensions.meta', 'markdown.extensions.extra'])
    html = m.convert(md.read())

content = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template('template.html').render(body=html, meta=m.Meta)

with open(outfile, 'w') as f: f.write(content)
