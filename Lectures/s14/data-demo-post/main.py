#!/usr/bin/env python
#
# this is a modified version of the Google App Engine Tutorial
import webapp2, os, urllib, urllib2, json, logging
import jinja2
import darksky_key

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

### Utility functions you may want to use
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)


def safeGet(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.URLError, e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code
        return None


def darkSkyREST(
    method = 'forecast',
    api_key = darksky_key.key,
    latlon=(47.6097,-122.3331),
    otherlist=None):
    url = "https://api.darksky.net/%s/%s/%s,%s"%(method,api_key,latlon[0],latlon[1])
    logging.info(url)
    return safeGet(url)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
        
    def post(self):
        template_values={}
        
        lat = self.request.get('lat',None)
        lon = self.request.get('lon',None)
        
        
        template_values = {}
        if lat != None and lon != None:
            res = darkSkyREST(latlon=(lat,lon))
            
            if res is not None:
                template_values["forecast"] = json.load(res)
                template_values["lat"] = lat
                template_values["lon"] = lon
            else:
                template_values['message'] = "Looks like things are broken. You searched for %s, %s. Did you enter a valid location?"%(lat,lon)
        
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([('/', MainHandler)], debug=True)