# A very simple script to generate a blog html page using jinja2.
import jinja2
import markdown
import argparse

# Parse arguments with arparse's help
parser = argparse.ArgumentParser()
parser.add_argument("infile", help="The markdown file.", type=str)
parser.add_argument("template", help="The template file.", type=str)
parser.add_argument("outfile", help="The name of the output file.", nargs='?', type=str)
args = parser.parse_args()

infile = args.infile
template = args.template
if args.outfile == None:
    outfile = 'out.html'
else:
    outfile = args.outfile

with open(infile, 'r') as md:
    m = markdown.Markdown(extensions=['markdown.extensions.meta', 'markdown.extensions.extra'])
    html = m.convert(md.read())

content = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template(template).render(body=html, meta=m.Meta)

with open(outfile, 'w') as f: f.write(content)

# TODO: Also it should generate an index page with all the posts and links to them.
