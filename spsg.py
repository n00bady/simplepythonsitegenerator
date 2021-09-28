# A very simple script to generate a blog html page using jinja2.
import jinja2
import markdown
import argparse
import os

# Parse arguments with arparse's help
parser = argparse.ArgumentParser()
parser.add_argument("template", help="The template file.", type=str)
args = parser.parse_args()

template = args.template

inpath = './_posts/'
outpath = './blog/'

for file in os.listdir(inpath):
    print("Processing:", file)
    # TODO: Make it check if they are indeed markdown files
    md = os.path.join(inpath, file)
    with open(md, 'r') as f:
        m = markdown.Markdown(extensions=['markdown.extensions.meta', 'markdown.extensions.extra'])
        html = m.convert(f.read())
    content = jinja2.Environment(loader=jinja2.FileSystemLoader('./')).get_template(template).render(body=html, meta=m.Meta)
    outfile = os.path.join(outpath, os.path.splitext(file)[0]+'.html')
    with open(outfile, 'w') as o: o.write(content)

# TODO: Also it should generate an index page with all the posts and links to them.
