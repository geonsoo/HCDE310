import os, webbrowser
from jinja2 import Template, Environment, FileSystemLoader
## you may have to install jinja
## sudo pip install Jinja2

jinja_environment = Environment(autoescape=True,
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

vals = {}
vals['department'] = "Human Centered Design & Engineering"
vals['university'] = "University of Washington"

template = jinja_environment.get_template('template.html')
html = template.render(vals)

fname = "mypage.html"
f = open(fname,"w")
f.write(html)
f.close()

## example 2
vals = {'department':{},'university':{}}
vals['department']['name'] = "Human Centered Design & Engineering"
vals['department']['url'] = "http://hcde.uw.edu/"
vals['university']['name'] = "University of Washington"
vals['university']['url'] = "http://www.uw.edu"

vals['programs']=["BS", 'MS', 'PhD','UCD Certificate']

template = jinja_environment.get_template('template2.html')
html = template.render(vals)

fname = "mypage2.html"
f = open(fname,"w")
f.write(html)
f.close()


## example 3, same values as above
template = jinja_environment.get_template('template3.html')
html = template.render(vals)

fname = "mypage3.html"
f = open(fname,"w")
f.write(html)
f.close()
