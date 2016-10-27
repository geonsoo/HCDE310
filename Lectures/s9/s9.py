import urllib2
response = urllib2.urlopen("http://smunson.com")
#print response.read()
# response.readlines gets the page as a list of lines
# we're only going to look at a few (slicing!)
for l in response.readlines()[69:84]:
    #rstrip to avoid extra spacing
    print l.rstrip()
    
print "\n"
    
print "\n\n ---- characters, lines, and info ----\n"
r = urllib2.urlopen("http://smunson.com")
print "Characters: %d"%(len(r.read()))
# note. reading consumes a response object so we have to reopen it each time
response = urllib2.urlopen("http://smunson.com")
print "Lines: %d"%(len(response.readlines()))
print "URL: %s"%response.geturl()
print "info:\n%s"%response.info()

print "\n\n ---- Beautiful Soup ----\n"
### BEAUTIFUL SOUP
from BeautifulSoup import BeautifulSoup

## first, get the file and store its contents as a string
htmlstring = urllib2.urlopen("http://hcde.uw.edu").read()

soup = BeautifulSoup(htmlstring)
## uncomment the next line to print all the HTML
## but it's a lot, so I left it commented.
#print soup.prettify()

## what's in the soup?
print soup.html.title
print soup.html.title.string

## how many paragraphs
print "Paragraphs: %d"%len(soup("p"))

## first paragraph?
print soup("p")[0]

## okay so that one was boring
print soup("p")[1]
print soup("p")[1].contents[0]

## all of the news headings
## look for an h3 with news and events
newsheader = soup.find("h3",text="Human Centered Design & Engineering News &amp; Events")

#now navigate to the next one
news = newsheader.parent.parent
articles = news.findNext("div")

for item in articles("div",{"class":"details"}):
        print item.h4.contents[0]
        print item.parent['href']
        
#easier way!
for item in soup("a",{"class":"news"}):
        print item.h4.contents[0]
        print item['href']