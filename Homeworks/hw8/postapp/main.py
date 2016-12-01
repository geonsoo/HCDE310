#Geon Soo Park


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
    api_key = '939bd2892135d413752e51d7e320b081',  #flickr_key.key,
    format = 'json',
    params={},
    printurl = False
    ):
    params['method'] = method
    params['api_key'] = api_key
    params['format'] = format
    if format == "json": params["nojsoncallback"]=True
    url = baseurl + "?" + urllib.urlencode(params)
    if printurl:
        print url
    else:
        return safeGet(url)

#
# Inputs:
#   tags: tags to search for
#   n: the number of search results per page (default value should be 5)
#  Returns: a list of (at most) n photo ids, or None if an error occured
# studied the solution and based on the feedback I changed my hw7

def getPhotoIDs(tags, n=5):
    result = flickrREST(params={"tags":tags,"per_page":n})
    if result is not None:
        jsonresult = result.read()
        d = json.loads(jsonresult)['photos']
        if d is not None:
            if d.has_key('photo') and len(d['photo']) > 0:
                return [photo['id'] for photo in d['photo']]
    
    return None

def getPhotoInfo(photoID):    
    result = flickrREST(method = 'flickr.photos.getInfo', params={'photo_id':photoID})
    if result is not None:
        jsonresult = result.read()
        info = json.loads(jsonresult)['photo']
        return info
    else:
        return None
        
        
def get_url(photo):
    return "https://farm%s.staticflickr.com/%s/%s_%s_q.jpg" % (photo["farm"], photo["server"], photo["id"], photo["secret"])

class MainHandler(webapp2.RequestHandler):
    def get(self):
        logging.info("In MainHandler")
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('searchinput.html')
        self.response.write(template.render(template_values))

class ResponseHandler(webapp2.RequestHandler):
    def post(self):
        vals = {}
        vals['page_title']="Search Photo"
        vals['photolist']= []
        name = self.request.get('username')
        go = self.request.get('gobtn') 
        if name:
            template = JINJA_ENVIRONMENT.get_template('response.html')
            photo_ids = getPhotoIDs(name)
            list_photo = []
            [list_photo.append(getPhotoInfo(i)) for i in photo_ids ] 
            photo_url = []
            [photo_url.append(get_url(j)) for j in list_photo]
            vals['username'] = photo_url
            logging.info(name)
            logging.info(go)
        
            self.response.write(template.render(vals))
            logging.info('name= '+ name)
            

# for all URLs except alt.html, use MainHandler
application = webapp2.WSGIApplication([ \
                                      ('/gresponse', ResponseHandler),
                                      ('/.*', MainHandler)
                                      ],
                                     debug=True)
