###### HCDE310, A15: Homework 6 application
### Geon Soo Park
import urllib, urllib2, json

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
        
def getArticle(sortBy):        
    baseurl = "https://newsapi.org/v1/articles"
    d = {'source':'techcrunch','sorBy': sortBy,'apiKey':'e28a0fa09e474b608d844ef74f3dbef1'}
    param_str = urllib.urlencode(d)
    wallstreet_request = baseurl + "?" + param_str
    wall_street = safeGet(wallstreet_request).read()
    wall_street_data = json.loads(wall_street)
    return wall_street_data
    
#this function gives the selected author's article title and description in
#selected articles

def getAuthors(articleCollection):
    authorSet = set();
    for each in articleCollection["articles"]:
        authorSet.add(each["author"])
    return authorSet
       
def printArticleInfo(category):
    articleCollection = getArticle(category)
    for each in articleCollection["articles"]:
        if each["author"] in getAuthors(articleCollection):
            print 'author: ' + each["author"]
            print 'title: ' + each['title']
            print 'description: ' + each['description'] + '\n' 
                            
category = ['top', 'latest', 'popular']               
for each in category:
    print "-------------------" + each + "-------------------"
    printArticleInfo(each)

