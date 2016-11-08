import urllib, urllib2, json, webbrowser

### Utility functions you may want to use
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

#### Main Assignment ##############

## Don't forget, you need to get your own api_key from Flickr, following the
#procedure in session 10 slides. Put it in the file flickr_key.py
# Then, UNCOMMENT the api_key line AND the params['api_key'] line in the function below.
import flickr_key
def flickrREST(baseurl = 'https://api.flickr.com/services/rest/',
    method = 'flickr.photos.search',
#    api_key = flickr_key.key,
    format = 'json',
    params={},
    printurl = False
    ):
    params['method'] = method
 #   params['api_key'] = api_key
    params['format'] = format
    if format == "json": params["nojsoncallback"]=True
    url = baseurl + "?" + urllib.urlencode(params)
    if printurl:
        print url
    else:
        return safeGet(url)

### This is where you should start filling in code...

## Building block 1 ###
# Define a function called getPhotoIDs() which uses the flickr API to search
# for photos with a given tag, and return a list of photo IDs for the
# corresponding photos. Use a list comprehension to generate the list.
# Hints: Use flickrREST(). You may wish to use print & pretty() to inspect
#       the data returned by flickr to figure out what fields to extract. You
#       may find useful code to copy and edit in s10.py, but make sure you
#       understand what it's doing!
#
#       flickrREST() defaults to the flickr.photos.search method, documented
#       at https://www.flickr.com/services/api/flickr.photos.search.html
#       This method will work for building block 1, but see the documentation
#       for what parameters you might pass.
#
# Inputs:
#   tag: a tag to search for
#   n: the number of search results per page (default value should be 100)
# Returns: a list of (at most) n photo ids, or None if an error occured




## Building block 2 ###
## Define a function called getPhotoInfo() which uses the flickr API to
# get information about a particular photo id. The information should be
# returned as a dictionary Hint: use flickrREST and the flickr API method
# flickr.photos.getInfo, documented at
# http://www.flickr.com/services/api/flickr.photos.getInfo.html
# Inputs:
#   photoID: the id of the photo you to get information about
# Returns: a dictionary with photo info, or None if an error occurred


## Building block 3 ###
## Define a class called Photo to represent flickr photos
# It should have at least three methods:
# (a) a constructor (init__())
# (b) a string representation (__str__())

## (a) __init__():
# The constructor (remember, the __init__() method is called the constructor)
# should take a dictionary representing photo info  and initialize
# eight instance variables:
#  -title: the title of the photo (Use "_content"!)
#  -author: the user that posted the photo (use username!)
#  -userid: the user nsid (####@N##, for example)
#  -tags: a list of tags (strings) associated with the photo (Use "_content"!)
#  -commentcount: a count with the number of comments on the photo
#  -numViews: the number of times the photo was viewed
#  -url: the location of the photo page on flickr
#  -thumbnailURL: the URL for a thumbnail of the image (150x150px square)
#
# Your constructor should use a list comprehension to create the tags list.
# Hint: You may wish to use print and pretty() to determine which fields in
#       the photo info dictionary to extract.
#       If a field needs to be converted to a number from a different type
#       (i.e. numViews), be sure to do that in the body of the constructor.

## (b) __str__()
# The __str__() method should return a string with the following format:
#   ~~~ <TITLE> ~~~
#   author: <AUTHOR>
#   number of tags: <NUMBER OF TAGS IN TAGS INSTANCE VARIABLE>
#   views <NUMBER OF VIEWS>
#   comments: <NUMBER OF COMMENTS>
# Look at HW 5 if you need reminders about doing this.
# Tip: use .encode('utf-8') on the title and author in case either
#          string contains unicode characters (strings that look like
#          u'something')


if __name__ == '__main__':
    ### Testing your building blocks
    print '\n\nTesting your building blocks\n------------'
    # test getPhotoIDs() with the following line of code, which will give
    # note the ids you get may be different than what's in the sample screenshot.
    #print getPhotoIDs('hamster', n=4)

    # Test getPhotoInfo() with the following two lines of code:
    #pd = getPhotoInfo(5140736446)
    #print pd

    # Test your Photo class with the following lines of code: Check the format
    # of your output against sample output in the PDF file, and make adjustments
    # to your __init__ and __str__ methods as needed
    #po = Photo(pd)
    #print po
    #print po.tags
    #webbrowser.open(po.url)
    


    ### Part 1 #########
    # Use your getPhotoIDs function to get a list of 100 photo ids with a tag of your choosing.
    # Convert the list of ids into a list of Photo objects using a list comprehension
    # You will need the getPhotoInfo() function to do this.
    # Pro tip: You may want to start out with the first 10 or 20 photos while
    #          testing. It takes a while to run.
    # Note: nothing gets printed out in this part. But you might want to do some
    # printing to check if it's working


    ### Part 2 #########
    # (a) Order the photo objects by number of views. Print the three most viewed photos
    print "\nTop Three Photos by Views"
    print "------------"

    # (b) Order the photo objects by number of tags. Print the three most tagged photos
    print "\nTop Three Photos by Number of Tags"
    print "------------"
    
    # (c) Order the photo objects by number of tags. Print the three most commented photos
    # NOTE: it is completely possible that you will have no photos with comments in your data set.
    print "\nTop Three Photos by Number of Comments"
    print "------------"

    ### Part 3 #########
    # Compute the total number of views received by each author in the photo
    # object list.  Then, print out the username of the author along with
    # the total number of views their photos had received, for the top ten
    # users, ranked in order of number of views, in the following format:
    # (1) Johnny 5: 1221
    # (2) Christina: 134
    # (3) Alex: 120
    # (4) Lucia: 113
    # (5) Michael: 108
    # (6) Cole: 104
    # (7) Ben: 98
    # (8) Stephanie: 54
    # (9) Joanna: 12
    # (10) Sean: 1
    print "\nTop ten authors by number of views"
    print "------------"
    
    ###  Part 4 #########
    ###  Output a HTML page with the top three images
    ###  for views, tags, and comments (from part 2).
    ###  Mininum reuqirements:
    ###  - header, title, and body tags
    ###  - text introducing each set of images 
    ###  - images tags with 150x150 thumbnails
    ###
    ###  We have not talked a lot about image tags, so this HTML may help:
    ###  <img src="{{thumbnailURL}}" alt="{{title}}"/>
    ###
    ###  We strongly encourage you to use Jinja, but you may instead use
    ###  code like we did for the photos from the Facebook group!
    ###
    ###  You may style your page as much as you like, but this is optional.
    ###
    ###  Fill in your code here
    
    # Based on the photos you get, which do you think is a better way to find
    # good photos, the ones with the most views or the most tags?
    print "------------"
    print """your thoughts here"""
    
