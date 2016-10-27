import urllib2

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