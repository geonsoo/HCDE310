
### LIST COMPREHENSIONS ###
## very Pythonic.

y = [x*x for x in [1, 2, 3]]
print y

# or
l =  [1, 2, 3]
y = [x*x for x in l]
print y


## they can use functions
#so rather than, 

print [3*x*x + 2*x - 7 for x in range(10)]

# we can do

def h(x):
    return 3*x*x + 2*x - 7

print [h(x) for x in range(10)]

# and rather than
def f(people):
    res = []
    for person in people:
        res.append("Hello " + person)
    return res
    
listOne = ['Alice', 'Bob', 'Carl']
for x in f(listOne):
    print x
    
# we can do
def g(people):
    return ["Hello " + person for person in people]
    
listOne = ['Alice', 'Bob', 'Carl']
for x in g(listOne):
    print x

## CYU
L = "Hello, everyone loves python".split()
# make a list consisting of just the first letters of each string in L (one line of code)

# your code here

## Filtering

## CYU
L = [3, 8, 9, 4, 2]
# make a list contianing the squares of the numbers in L that are divisible by 3

# your code here

### FUNCTIONS AS FIRST CLASS OBJECTS ##
def g(a, b):
    return a+b
    
print type(g)
print g
print g(3,4)

## Lambdas
# like a function, but not

# theye have the form
# lambda <parameter list>: <expression>
# and will return the <expression> computed for given parameters

h = lambda x: x + 1
print type(h)
print h
print h(3)
print (lambda x, y: x+y)(5, 4)

L = [g, h]         # a list of our functions from above
print L[0](6,7)
print L[1](8)
L[1] = lambda x:x-1
print L[1](8)

polys = [lambda x: x, lambda x: x**2, lambda x: x**3]
for func in polys:
    print func(2)
    
# CYU
d = {'a':g,'b':lambda x, y: y-x}
# what will this print?
print d['b'](9,10)

## functions as returned values
def make_incrementor(n):
    return lambda x: x+n

x = make_incrementor(42)
print x(2)

## making a list of functions with list comprehensions
def make_poly(exponent):
    return lambda x: x**exponent
    
polys = [make_poly(i) for i in range(10)]
for func in polys:
    print func(2)
# or 
print [func(2) for func in polys]

## functions as parameter values
def apply_fn(f, x):
    return f(x)

print apply_fn(abs, -3)
print apply_fn(lambda x: x*x, 3)

# CYU
print apply_fn(make_incrementor(3), 10)

### The main event: Sorting ###
def basicSorts(g):
    print "g is ", g
    print "sorted copy", sorted(g)
    print "reverse sorted copy", sorted(g, reverse = True)
    print "original g unchanged", g
    g.sort()
    print "g has changed after sort method", g
    
g = [5, 6, -3, -2, 7, 1, 0]
basicSorts(g)

##sorting with a key function
def myAbs(x):
        print "in myAbs, the decorator is", x
        return abs(x)

print "running sorted with key = myAbs"
g3 = sorted(g, key=myAbs)
print "the sorted reesult is g3"

# if we didn't are about printing, we could have just used abs
g3 = sorted (g, key=abs)

g = [5, 6, -2, -7, 1]
print "running sorted with key - lambda x: -x"
g3 = sorted(g, key=lambda x: -x)
print "the sorted result is", g3

# exercise
L = "This is a bag of words of various lengths".split()
print L
# write code to sort the words in L based on their lengths

# your code here.

## sorting with a comparison function
def compAbs(x, y):
    print "in compAbs", x, y
    if abs(x) < abs(y):
        return -1
    elif abs(x) == abs(y):
        return 0
    else:
        return 1
        
print "running sorted with cmp = compAbs"
g2= sorted(g, cmp=compAbs)
print "the sorted result is", g2

## this isn't terribly interesting since we could have just done
#g2= sorted(g, key = abs)
## but it matters more for objects.

# CYU - what will this print?
g = [5, 6, -2, -7, 1]
print "running sorted with cmp = lamdba x, y: y-x"
g3 = sorted(g, cmp=lambda x, y: y-x)
# print "the sorted result is", g3

# CYU
# write code to sort a list of of numbers
# x before y if abs(x-3) < abs(y-3)

## sorting dictionaries.
def sortKeysByValue(d):
    ks = d.keys()
    return sorted(ks, key= lambda k: d[k])

d2 = {'a' : 3, 'b': 6, 'c': -1, 'd': 0}
for k in sortKeysByValue(d2):
    print "key is %s; value is %d" % (k, d2[k])



