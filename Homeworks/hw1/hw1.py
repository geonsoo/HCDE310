# Geon Soo Park
# HCDE 310
# HW1


lst = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
#fname = "test.txt"
fname = "/Users/CalebP/CourseFiles/Homeworks/hw2/hw2feed.txt"
#fname = raw_input("Please enter a file name: ")
numChars = 0
numLines = 0
numWords = 0

file_name = open(fname, 'r')
for line in file_name.readlines():
    numLines += 1
    for word in line.split():
        numWords += 1
    for chr in line:
        numChars += len(chr)

# output code below is provided for you; you should not edit this
print numChars, 'characters'
print numLines, 'lines'
print numWords, 'words'
#fname = "test.txt"
fname = "/Users/CalebP/CourseFiles/Homeworks/hw2/hw2feed.txt"
#fname = raw_input("Please enter a file name: ")
numChars = 0
numLines = 0
numWords = 0

file_name = open(fname, 'r')
for line in file_name.readlines():
    numLines += 1
    for word in line.split():
        numWords += 1
    for chr in line:
        numChars += len(chr)

# output code below is provided for you; you should not edit this
print numChars, 'characters'
print numLines, 'lines'
print numWords, 'words'
otherlst = ['a','b','c','d','e','f','g']
s = "This is a test string for HCDE 310"

#Exercise 1 (working with a list):
#a.Print the first element of lst

print lst[0]

#b.Print the last element of otherlst

print otherlst[-1]

#c.Print the first five elements of lst
print lst[0:5]

#d.Print the fifth element of otherlst
print otherlst[4]

#e.Print the number of items in lst
print len(lst)

#Exercise 2 (working with a string):
#a.Print the first four characters of s
print s[0:4]

#b.Using indexing, print the substring "test" from s
print s.split()[3]

#c.Print the contents of s starting from the 27th character (H)
print s[26:]
        
#d.Print the last three characters of s
print s.split()[-1]

#e.Print the number of characters in s
print len(s)


