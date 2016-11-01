import json

###################
### utility functions-- don't edit these; just call them as needed
### the first two should be familiar from  hw5-buildingblocks.py
def pretty(obj):
    return json.dumps(obj, sort_keys=True, indent=2)

def shortname(username):
    """returns the abbreviated version of a username"""
    ss = username.split()
    return '%s %s.' % (ss[0], ss[-1][0])


def genPicturePage(post_objects, filename):
    """generates a web page from a list of picture objects
     inputs:
       post_objects: a list of Post objects
       filename: output html file
    """
    out = open(filename, 'w')
    out.write('<html><head><title>HCDE310 Pictures</title></head>\n') 
    out.write('<body>\n')

    img_template = '<a href="%s" title="%s"><img src="%s"/ alt="image from %s"></a>\n'
    for post in post_objects:
        if isinstance(post, Picture):  # only write out Picture posts
            out.write(img_template % (post.link, post.name, post.preview_url, post.name))

    out.write('</body></html>')
    out.close() 


###################
### Class 1: the Post class
class Post():
    """object representing status update"""
    def __init__(self, pd):
        # self.message is the instance variable containing the post's message
        # some posts do not have messages so we set it to a blank string.
        self.message = pd.get('message','')

        # if the post dictionary has a 'comments' key, set self.comments to the
        # corresponding comments dictionary. otherwise, set self.comments to None
        if 'comments' in pd:
            self.comments = pd['comments']
        else:
            self.comments = {"data":[]}
     
        # if the post dictionary has a 'likes' key, set self.likes to
        # the corresponding likes dictionary.  otherwise, set self.likes to None
        if 'likes' in pd:
            self.likes = pd['likes']
        else:
            self.likes = {"data":[]}

    # (a): fill in code here to initialize the name instance variable
    #      to the short name of the user in the post dictionary. 
    #      Hint: see your poster() function from hw5-buildingblocks.py
    #      then uncomment the testing line in the main block at the end of the file

        self.name = shortname(pd['from']['name'])

    # (b): Write a method to return the comments count.
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
    def commentCount(self):
        """returns the number of comments"""
        # (b): fill in code here. 
        return len(self.comments['data'])
     
    # (c): Write a method to return the likes count.
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
    def likeCount(self):
        """returns the number of likes"""
        # (c): fill in code here.
        return len(self.likes['data'])

    # (d): Some messages are longer than 140 characters. If so, write a
    #      method to return a short message that consists of the first
    #      137 characters of the message plus elipses, e.g.
    #      "the first 137 characters..."
    #      Uncomment the following two lines, and also the
    #      corresponding line in the main block (below)
    def shortMessage(self):
        """returns the message (if less than 140 characters) or a shortened message (137 characters plus ...) if the message is longer than 140 characters)"""
        # (d) fill in code here.
        if len(self.message) > 140:
            return self.message[:137]+"..."
        else: 
            return self.message

    def __str__(self):
        """string representation of the post"""
        s = '--- post ---------\n'
        # uncomment the following lines after you write and test (a-d) [e]
        s += 'name: %s\n' % self.name                  # (a)
        s += 'comments: %s\n' % self.commentCount()  # (b)
        s += 'likes: %s\n' % self.likeCount()        # (c)
        s += 'message: %s\n' % self.shortMessage()    # (d)
        return s

#     uncomment the following two lines
    def hasQuestion(self):
        """returns True if the message contains a '?'."""
        #(f) fill in code here
        if "?" in self.message:
            return True
        return False


### Building Block 2: the Picture class
class Picture(Post):
    """object representing a Picture post"""
    ## The init method for Picture() calls the init method 
    ## from Post, but also sets instance variables for
    ## a link and a preview URL.
    
    def __init__(self, postdict):
        Post.__init__(self, postdict)
        self.preview_url = postdict['picture']
        self.link = postdict['link']

    def __str__(self):
#         fill in code here. (3.a)
#         the string being returned should be similiar to that of Post.__str__()
#         except it should also print out the linked picture's preview URL
#         and link URL (see PDF for details)

        poststr = "--- picture post"+Post.__str__(self)[18:]
        return "%spreview url: %s\nlink: %s\n"%(poststr,self.preview_url,self.link)


### Main block
if __name__ == '__main__':  
    # this loads the facebook group data as a list of dictionaries
    postdicts = json.load(open('hw5feed.json'))['data']

    print "-- TEST 1 --"
    ### Test 1: polymorphism with  __str__() methods
    # sample Posts to print
    # this post is short (< 140 chars)
    my_post_short = Post(postdicts[72])
    # this post is long (> 140 chars)
    my_post_long = Post(postdicts[61])

    print "- elements -"
    # uncomment the following lines as you implement building block 1a-d:
    print "my_post_short poster:        %s"%my_post_short.name             # tests (1a)
    print "my_post_short comment count: %s"%my_post_short.commentCount()   # tests (1b)
    print "my_post_short like count:    %s"%my_post_short.likeCount()      # tests (1c)
    print "my_post_short message:       %s"%my_post_short.shortMessage()   # tests (1d)
    print "my_post_long  message:       %s"%my_post_long.shortMessage()    # tests (1d)
    
    # uncomment the following two lines to test (1e)
    print "- short post -"
    print my_post_short
    print "- long post -"
    print my_post_long
    
    
    # testing building block 2
    mypic = Picture(postdicts[1])
    print mypic                     # tests (3a)

    # convert all dictionaries to Post, Picture, and Link objects
    postobjects = []  # start off with empty list of objects
    for postdict in postdicts:
        # make a Post, Picture, or Link object from the post dictionary depending
        # on the value of the "type" key in the post dictionary
        if postdict.has_key('picture'):
            postobject = Picture(postdict)
        else:
            postobject = Post(postdict)  
         
        # add the post object to the list
        postobjects.append(postobject)

    ### Test 2: Outputting Picture objects as a web page: (testing 3a,b)
#    uncomment the following line of code and verify that hcde310pictures.html
#    displays thumbnail images that link back to the respective facebook picture
#    include hcde310pictures.html in your Canvas upload

    genPicturePage(postobjects, 'hcde310pictures.html')

    ### Task 1: printing questions
    print ";;;;; Task: printing questions ;;;;;;;"
    first25 = postobjects[:25]  # sample set of posts
    # fill in code here that prints just the questions and number of
    # comments received in the first 25 items in postobjects
    # Print your output as (also see PDF):  
    #    Short name received # replies to their question:
    #    short message
    # hint: use your .hasQuestion() method
    for post in first25:
        if post.hasQuestion():
            print "%s received %d replies to their question:\n%s"%(post.name,post.commentCount(),post.shortMessage())
    

    ### Task 2: counting and printing totals  (this is optional but strongly recommended for review)
    print ";;;;; Post, Comment, and Like counts per person ;;;;;;;"
    # Loop through postobjects and count the number of posts made by each person
    # and the number of comments and likes they *received*
    # You may either use a dictionary for this or create a new class for a person
    # If you create a dictionary (you are most familiar with these),  
    # it should be in the format {Name:  {'posts':n,'comments':y,'likes':z},
    #                             Name2: {'posts':n,'comments':y,'likes':z},
    #                            ... }
    
    class Person():
        def __init__(self,name):
            self.name = name
            self.posts = 0
            self.comments = 0
            self.likes = 0
        def processPost(self,post):
            self.likes += post.likeCount()
            self.comments += post.commentCount()
            self.posts +=1
        def __str__(self):
            return "%s posted %d times and received %d comments and %d likes"%(self.name,self.posts,self.comments,self.likes)

    people = {}
    for post in postobjects:
        if post.name not in people:
            people[post.name] = Person(post.name)
        people[post.name].processPost(post)
    
    
    # then, write code to loop through your posters and print their totals
    # in the format:
    # Name posted n times and received y comments and z likes.
    for person in people.values():
        print person
