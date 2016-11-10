#!/usr/bin/env python
#
# this is a modified version of the Google App Engine Tutorial
import webapp2, os, urllib
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))



application = webapp2.WSGIApplication([('/', MainHandler)], debug=True)