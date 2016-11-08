f = open("/Users/CalebP/CourseFiles/Lectures/s4/sherlock.txt",'r')
fstring = f.read()    #assign fstring long string with the whole file


# This is a function that will replace (most) punctuation
# you'll see it again in the homework
def stripWordPunctuation(word):
    return word.strip(".,()<>\"\\'~?!-;*/")

wordlist = fstring.split()

### Challenge 0: count the number of times the words
### elementary and obviously appear in Sherlock Holmes
### note that we have already opened, read, and split the
### file for you above

### fill in your code here

total = 0

for x in wordlist:
    if x.lower() == 'elementary' or x.lower() == 'obviously':
        total += 1
    
print total

### Challenge 1: modify the code below to print
### all of the words that appear more than 10 times
### and the number of times they appear
###
###
### Challenge 2: modify and add to your code
### to print the word that appears the most.
### Extra challenge 1: make all words lower case first.
### Extra challenge 2: remove punctuation using 
###                    stripWordPunctuation()

freqs = {}            #an empty dictionary to keep track of frequency
# tally

# print tally
# printing only words appearing more than 10 times