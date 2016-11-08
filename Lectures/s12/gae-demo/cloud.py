import webapp2, os, urllib, logging
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #print statements don't work well
        #print "In MainHandler"
        logging.info("In MainHandler")
        
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class AltHandler(webapp2.RequestHandler):
    def get(self):
        template_values = {}
        template_values['title']='Term Cloud Page'
        freqs={'Popular':12, 'Unpopular':2, 'Platinum':24, 'Medium':6}
        template_values['terms']=freqs.items()

        template = JINJA_ENVIRONMENT.get_template('tagcloud.html')
        self.response.write(template.render(template_values))


application = webapp2.WSGIApplication([('/alt.html', AltHandler),('/', MainHandler)], debug=True)
