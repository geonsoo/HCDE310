class Dog:
    """A slobbering friend"""
    
    def __init__(self,n):
        """Initialize with number of woofs"""
        self.woofcount = n
    def bark(self):
        """Bark out loud"""
        for i in range(self.woofcount):
            print "Woof"
        
print "Dog has type", type(Dog)
print "Dog.bark has type", type(Dog.bark)

gromit = Dog(12)
print type(gromit)
print gromit.__class__.__name__
print gromit.__class__ == Dog
print gromit.woofcount

print "\n===gromit.bark()==="
gromit.bark()

Woofus = Dog(1)
print Woofus.woofcount
Woofus.bark()
print "----"
Woofus.woofcount = 2
print Woofus.woofcount
Woofus.bark()


Fluffy = Dog(1, "Ruff")
Woofus = Dog(3)
Rover = Dog (4, "Arf")
