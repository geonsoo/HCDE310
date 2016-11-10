import urllib2, json, urllib
import jinja2, os

#tell python where to look for template
JINJA_ENVIRONMENT = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


### flickrREST from s10

def flickrREST(baseurl='https://api.flickr.com/services/rest',
        method = 'flickr.photos.search',
        api_key = '#FILL THIS IN',
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

def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def lookupweather(loc):
    baseurl = "https://api.darksky.net/forecast/"
    key = "#FILL THIS IN"
    url = "%s%s/%s,%s"%(baseurl,key,loc[0],loc[1])
    #print "fetching %s"%url
    return safeGet(url)

def makePhotoURL(pd):
    #print pd
    ## get a photo url, following documentation at https://www.flickr.com/services/api/misc.urls.html
    ### You will need to fill this in!
    return ""

def returnPhoto(loc,fd):
    currently = fd['currently']
    summary = currently['summary']

    # search for photos tagged with the summary, near the location (max 20 km)
    result = flickrREST(params={"tags":summary,"per_page":1,"lat":loc[0],"lon":loc[1],"radius":20})
    
    # if we have results, get a photo. otherwise just use an empty string for now
    if result is not None:
        resultjson = json.load(result)
        #print pretty(resultjson)
        photourl = makePhotoURL(resultjson['photos']['photo'][0])
    else:
        photourl = ""
    
    return photourl

######################

if __name__=="__main__":
    # my family locations. 
    familylocs = {'brother':(40.801936,-73.961034),'parents':(43.199404,-70.865250)}
        
    #template data, with empty list for family members
    tvals = {'family':[]}
    
    for family in familylocs:
        forecast = lookupweather(familylocs[family])
        if forecast is not None:
            fd = json.load(forecast)
            
            #just add additional family data to forecast member dictionary
            fd['photo'] = returnPhoto(familylocs[family],fd)
            fd['name'] = family
            
            #now add it to the list
            tvals['family'].append(fd)
            
    # load template and write file
    f = open("darkskyoutput.html",'w')
    template = JINJA_ENVIRONMENT.get_template('darksky.html')
    f.write(template.render(tvals))
    f.close()
