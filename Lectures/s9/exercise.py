import urllib2
from BeautifulSoup import BeautifulSoup

def try_it(someURL):
    # Get the web page at that URL
    response = urllib2.urlopen(someURL)

    # Read the page data as one big string
    page_data = response.read()

    # Print out the URL
    print "URL is: " + response.geturl()

    # Print out the number of characters
    print "# of characters: " + str(len(page_data)) + "\n"

    # Print out some extra information
    print "--- info ---"
    print response.info()

def soupIt(someURL):
    # note, the next line won't work until you have installed
    # BeautifulSoup. See s11.py or the slides for instructions
     
    htmlstring = urllib2.urlopen(someURL).read()
    soup = BeautifulSoup(htmlstring)
    
    # now do something interesting here
    # to figure out what to do, maybe view the source 
    # of the URL to learn the structure of the page

### Main block
if __name__ == '__main__':

    print "\n----- PART 1 -----"
    # The URL I want to use
    myURL = "http://hcde.washington.edu"

    # Call try_it with myURL
    try_it(myURL)


    print "\n----- PART 2 -----"
    # Uncomment the next two lines and set the URL to "http://www.google.com"
    #myURL = "WHAT GOES HERE"
    #try_it(myURL)


    print "\n----- PART 3 -----"
    # This time, replace PICKSOMETHING with an address of your choice.
    # Remember to include the "http://"

    #myURL = "PICKSOMETHING"
    #try_it(myURL)

    print "\n----- Let's make this more interesting? -----"
    # (1) Uncomment the next code, pick a URL
    # (2) fill in the function soupIt(myURL)to do something interesting
    #myURL = "PICKSOMETHING"
    soupIt(myURL)
