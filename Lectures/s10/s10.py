### safeGet from last time
def safeGet(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.URLError, e:
        if hasattr(e,"code"):
        	print "The server couldn't fulfill the request."
        	print "Error code: ", e.code
        elif hasattr(e,'reason'):
        	print "We failed to reach a server"
        	print "Reason: ", e.reason
        return None
    
## use this function to make more readable output of nested data structures
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

###########################
### the flickr rest API ###
import urllib

def flickrREST(baseurl='https://api.flickr.com/services/rest',
        method = 'flickr.photos.search',
        api_key = '#sign up at https://www.flickr.com/services/apps/create/apply/ and fill yours in here',
        format = 'json',
        params = {},
        printurl = False
        ):
    params['method'] = method
    params['api_key'] = api_key
    params['format'] = format
    if format == "json":
        params['nojsoncallback'] = True
    url = baseurl+ "?" + urllib.urlencode(params)
    if printurl:
        print url
    return safeGet(url)
    
result = flickrREST(params={"tags":"mountains","per_page":10},printurl=True)
print result.read()

# processing JSON result
import json
result = flickrREST(params={"tags":"mountains","per_page":10})
jsonresult = result.read()
d = json.loads(jsonresult)
print pretty(d)
print d.keys()
print d['photos'].keys()
photos = d['photos']['photo']
print len(photos)
for k in photos[0]:
    print k
    
import webbrowser
## bet you didn't see that coming
for photo in photos:
    owner = photo['owner']
    id = photo['id']
    url = 'http:/www.flickr.com/photos/%s/%s'%(owner,id)
    webbrowser.open(url)