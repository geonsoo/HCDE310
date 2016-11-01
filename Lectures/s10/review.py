def hello(who, count = 2):
    print "He said hello to %s %d times in all" % (who, count)
    return None

# How would you call hello in a way that generates the following outputs?
# He said hello to me 5 times in all

# He said hello to the world 10 times in all

# He said hello to everyone 2 times in all

# He said hello to us twice in all
# You can't do it with the hello function!!

x = 3.5
y = "watermelons"
# How would you use string interpolation (templates) to generate the string
# "I'd like to buy 3.5 oranges and 2 watermelons" ?


class Dog:
    """A slobbering friend"""

    def __init__ (self, n, barktype="Woof"):
        """Initialize with number of woofs"""
        self.woofcount = n
        self.barktype = barktype
    def bark (self):
        """Bark out loud"""
        for i in range(self.woofcount):
            print self.barktype
            #print "woof"
#1) add a method beg, which prints out the phrase "food please" and then barks
#   however the dog barks


#2) create instances of Dog, and have it beg.
snuffy = Dog(7, "yap")
snuffy.beg()


#3) practice with lists
x = [1, 2, 3]
# print 3 from list x

x.append(0)
x.append(5)

# what is the length of x now? (print len(x) to check)
# what are the contents of list x now? (print it to check)

x.extend([9, 10])
# what is the length of x now? (print len(x) to check)
# what are the contents of list x now? (print it to check)

x.append([9, 10])
# what is the length of x now? (print len(x) to check)
# what are the contents of list x now? (print it to check)
