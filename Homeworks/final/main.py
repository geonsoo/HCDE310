import webapp2, urllib, urllib2, json
import jinja2
import os
import logging
import time, datetime

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def safeGet(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.HTTPError, e:
        print "The server couldn't fulfill the request." 
        print "Error code: ", e.code
    except urllib2.URLError, e:
        print "We failed to reach a server"
        print "Reason: ", e.reason
    return None

def yahooFinanceREST(
    baseurl = 'http://chartapi.finance.yahoo.com/instrument/1.0/',
    params={},
    stock=
    method = '/chartdata;type=quote;range=10d/csv'
    ):
    
    url = baseurl + stock + method
    print url
    return safeGet(url)

yahooFinanceREST(params={'stock':'GOOG'})

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #print statements don't work well
        #print "In MainHandler"
        logging.info("In MainHandler")
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('home.html')
        self.response.write(template.render(template_values))    
    
class HomeHandler(webapp2.RequestHandler):
    def post(self):
        #search = 'puppies'
        search = self.request.get('search')
        '''idlist = getPhotoIDs(search, n=50) 
        newidlist = [getPhotoInfo(id) for id in idlist]
        viewsidlist = sorted(newidlist, key=lambda e: int(e["photo"]["views"]), reverse=True)
        photolist = []
        for i in range(16):
            photolist.append(Photo(viewsidlist[i]))'''
            
        vals = {}
        vals['page_title']="Investment Calculator"
        
        
        go = self.request.get('gobtn') 
        logging.info(search)
        logging.info(go)
        if search:
            # if form filled in, greet them using this data
            vals={'name':search}
            template = JINJA_ENVIRONMENT.get_template('result.html')
            self.response.write(template.render(vals))
            logging.info('search= '+search)
        else:
            #if not, then show the form again with a correction to the user
            vals['prompt'] = "How can I help you if you don't enter a company?"
            template = JINJA_ENVIRONMENT.get_template('home.html')
            self.response.write(template.render(vals))
    

# for all URLs except alt.html, use MainHandler
application = webapp2.WSGIApplication([ \
                                      ('/data', HomeHandler),
                                      ('/.*', MainHandler)
                                      ],
                                     debug=True) 

