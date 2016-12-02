#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import urllib, urllib2, webbrowser, json
import os
import logging

JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

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


def flickrREST(baseurl = 'https://api.flickr.com/services/rest/',
               method = 'flickr.photos.search',
               api_key = '939bd2892135d413752e51d7e320b081',
               format = 'json',
               params={},
               printurl = False
               ):
    params['method'] = method
    params['api_key'] = api_key
    params['format'] = format
    params['sort'] = 'interestingness-desc'
    if format == "json": params["nojsoncallback"]=True
    url = baseurl + "?" + urllib.urlencode(params)
    if printurl:
        print url
    else:
        return safeGet(url)
        
def getPhotoIDs(tags="Seattle",n=100):
    resp = flickrREST(params={"tags":tags,"per_page":n})
    if resp is not None:
        photosdict = json.loads(resp.read())['photos']
        if photosdict is not None:
            if photosdict.has_key('photo') and len(photosdict['photo']) > 0:
                return [photo['id'] for photo in photosdict['photo']]
    return None


def getPhotoInfo(photoID):
     resp = flickrREST(method="flickr.photos.getInfo",params={"photo_id":photoID})
     if resp is not None:
         return json.loads(resp.read())['photo']
     else:
        return None
     

class Photo():
    def __init__(self,pd):
        self.title=pd['title']['_content'].encode('utf-8')
        self.author=pd['owner']['username'].encode('utf-8')
        self.userid = pd['owner']['nsid']
        self.tags = [tag["_content"] for tag in pd['tags']['tag']]
        self.numViews = int(pd['views'])
        self.commentcount = int(pd['comments']['_content'])
        self.url = pd['urls']['url'][0]['_content']
        self.thumbnailURL = self.makePhotoURL(pd)

    def makePhotoURL(self,pd,size="q"):
        ## get a photo url, following documentation at https://www.flickr.com/services/api/misc.urls.html
        url = "https://farm%s.staticflickr.com/%s/%s_%s_%s.jpg"%(pd['farm'],pd['server'],pd['id'],pd['secret'],size)
        return url
        
    def __str__(self):
        return "~~~ %s ~~~\nauthor: %s\nnumber of tags: %d\nviews: %d\ncomments: %d"%(self.title ,self.author ,len(self.tags),self.numViews,self.commentcount)



class MainHandler(webapp2.RequestHandler):
    def get(self):
        #print statements don't work well
        #print "In MainHandler"
        logging.info("In MainHandler")
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('greetinput.html')
        self.response.write(template.render(template_values))
'''
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
'''

class GreetResponseHandler(webapp2.RequestHandler):
    a = flic
    def post(self):
        vals = {}
        vals['page_title']="Greeting Page Response"
        vals['photolist']= []
        name = self.request.get('username')
        go = self.request.get('gobtn') 
        logging.info(name)
        logging.info(go)
        if name:
            # if form filled in, greet them using this data
           # greet_types = self.request.get_all('greet_type')
          #  logging.info(greet_types)
            #vals['greetings'] = [greet_person(name, t) for t in greet_types]
            template = JINJA_ENVIRONMENT.get_template('response.html')
            self.response.write(template.render(vals))
            logging.info('name= '+name)
            
        #else:
            #if not, then show the form again with a correction to the user
         #   vals['prompt'] = "How can I greet you if you don't enter a name?"
          #  template = JINJA_ENVIRONMENT.get_template('greetform.html')
           # self.response.write(template.render(vals))
    

# for all URLs except alt.html, use MainHandler
application = webapp2.WSGIApplication([ \
                                     # ('/greetings', GreetHandler),
                                      ('/gresponse', GreetResponseHandler),
                                     # ('/hello.html', HelloHandler),
                                      ('/.*', MainHandler)
                                      ],
                                     debug=True)
