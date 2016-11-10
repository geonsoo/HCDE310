#!/usr/bin/env python

import webapp2, os, urllib
import jinja2

import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("In MainHandler")
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        vals = {}
        vals['page_title']="Hello page"
        logging.info(type(self))
        req = self.request
        logging.info(type(req))
        vals['url']= req.url
        ## for url paths that look like /hello.html?n=4&name=you
        n = int(req.get('n', 1))
        name = req.get('name', 'world')
        vals['greeting']="Hello " + name
        vals['counter_list']= range(n)
        template = JINJA_ENVIRONMENT.get_template('hello.html')
        self.response.write(template.render(vals))
        

class GreetHandler(webapp2.RequestHandler):
    def get(self):
        vals = {}
        vals['page_title']="Greeting form"
        template = JINJA_ENVIRONMENT.get_template('greetform.html')
        self.response.write(template.render(vals))

def greet_person(name, t):
    if t == "birthday":
        return "Happy Birthday this month,  %s!" % (name)
    else:
        return "Hello %s" % (name)

class GreetResponseHandler(webapp2.RequestHandler):
    def get(self):
        vals = {}
        vals['page_title']="Greeting Page Response"
        name = self.request.get('username')
        go = self.request.get('gobtn') 
        logging.info(name)
        logging.info(go)
        if name:
            # if form filled in, greet them using this data
            greet_types = self.request.get_all('greet_type')
            logging.info(greet_types)
            vals['greetings'] = [greet_person(name, t) for t in greet_types]
            template = JINJA_ENVIRONMENT.get_template('greetresponse.html')
            self.response.write(template.render(vals))
            logging.info('name= '+name)
        else:
            #if not, then show the form again with an angry correction to the user
            vals['prompt'] = "How can I greet you if you don't enter a name?"
            template = JINJA_ENVIRONMENT.get_template('greetform.html')
            self.response.write(template.render(vals))
    

# pick handlers based on URL
application = webapp2.WSGIApplication([ \
                                      ('/greetings', GreetHandler),
                                      ('/gresponse', GreetResponseHandler),
                                      ('/hello.html', HelloHandler),
                                      ('/.*', MainHandler)
                                      ],
                                     debug=True)


