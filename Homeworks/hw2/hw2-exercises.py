#Geon Soo Park
# HCDE 310

### exercises
# Part 3
s = "This is a test string for hw2."
lst = [1, 2, 3, 4, 5, 6]

print "=1="
# 1: iterated operation over list

# Write code that iterates over each element of lst using a for loop, printing
# each element on a new line
for number in lst:
    print number

print "=2="
# 2: summing values of a list
# Write code that adds up all the elements of lst
# using a for loop, then prints out the sum. (hint: you will need to add to the
# variable total at every step of the for loop)
#
# Note: this is the example I used to teach you the accumulation pattern in
# lecture. Try to reconstruct the code here without looking at that code.
# You'll be glad for working through it do it when you get to part III of
# this HW and have to use the accumulation pattern in a more creative way.
# fill in the rest here

total = 0
for number in lst:
    total += number
print total


print "=3="
# 3: splitting strings
# Write code that splits s into a list separate words
# (where each word is defined to be any series of characters separated by a
# whitespace). Print out the list using a for loop (as in (1)), one word per line.

for each_word in s.split():
    print each_word
    
print "=4="
# 4: replacing an element of a list
# Replace the element of lst whose value is four with the value 'four' and
# then print lst (you can do this with indexing if you like)

lst[3] = 'four'
print lst

print "=5="
# 5: print out a file, verbatim
# Read and print each line contained in 'test.txt'.  Your program should
# output the text exactly as it is in test.txt.
# (Hint: you may need to use rstrip() to remove the newline character at the end
# of each line, to avoid getting an extra blank line between each real line.)


fname = "/Users/CalebP/CourseFiles/Homeworks/hw2/test.txt"
#fname = "test.txt"  
file_name = open(fname, 'r').read()
print file_name

# fill in the rest here

print "=6="
# 6: print out only items containing a certain string
# (see instructions for parts 6a, 6b, 6c)

dogList = ["Akita","Alaskan Malamute","Australian shepherd","Basset hound","Beagle","Boston terrier","Bulldog","Chihuahua","Cocker Spaniel","Collie","French Bulldog","Golden Retriever","Great Dane","Poodle","Russell Terrier","Scottish Terrier","Siberian Husky","Skye terrier","Smooth Fox terrier","Terrier","Whippet"]

print "==6a=="
# 6a iterate over dogList. print out where in each line the string Terrier can be found
# (if it cannot be found, print -1). hint: use find() (see supplement two)
# Case does not matter. It should match "Terrier" or "terrier"
for dog_name in dogList: 
    print dog_name.lower().find('terrier')

print "==6b=="
#6b:
binList = [0,1,1,0,1,1,0]

# Iterate over binList. If the current item equals 1
# print "One". Otherwise, don't print anything.
for number in binList:
    if number == 1:
        print 'One'

print "==6c=="
# 6c
# now, iterate over dogList. print out only the items that contain the string Bulldog
# case does not matter, you should match bulldog or Bulldog
# hint: You will need to use if. Also, find() may help.
for find_dog in dogList:
     if find_dog.lower().find('bulldog') != -1:
        print find_dog