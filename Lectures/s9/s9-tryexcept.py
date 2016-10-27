## try/except and arithmetic
try:
    x = 1/0
except ArithmeticError, detail:
    print "Handling run-time error", detail
print "still running, affer handling an error"
print "hooray!"

# outside of the try/except, though, we'd get an error that
# crashes are wonderful program, so I commented it out
#x = 1/0

## try/except with urllib2
import urllib2

def try_url_demo(url):
    print '\ntrying to fetch', url
    try:
        response = urllib2.urlopen(url)
    except urllib2.URLError, e:
        if hasattr(e,'reason'):
            print "We failed to reach a server"
            print "Reason", e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request."
            print "Error code: ", e.code
    else:
        ## this else goes with the try/except
        ## everything is find, got the page
        print "got", response.geturl()
        
# n.b.: not a website is actually a website
try_url_demo("http://www.notawebsite.com")
# actual website
try_url_demo("http://hcde.washington.edu")
# this one isn't unless someone in section A
# buys it and sets it up before Section B
try_url_demo("http://www.notawebsiteatall.com")
## this is a real server but no page at the address
try_url_demo("http://hcde.washington.edu/stuff")

def safeGet(url):
    try:
        return urllib2.urlopen(url)
    except urllib2.URLError, e:
        if hasattr(e,'reason'):
            print "We failed to reach a server"
            print "Reason", e.reason
        elif hasattr(e,"code"):
            print "The server couldn't fulfill the request."
            print "Error code: ", e.code
        return None
    
if safeGet("http://hcde.washington.edu") is not None:
    print "yay, we got the website. and could do things with it"
else:
    print "Sadface, no page available"
    ## alternatively, we could:
    ##    (a) try again
    ##    (b) load a cached (static) version of the file from disk

