import re
#######################################################################################################################
# STEP: ONE
# TITLE: Do you have python working?
# INSTRUCTIONS: uncomment the print statement and run it

# THE CODE:
#print("Hello pyladies oakland! Together we can do anything!")

#######################################################################################################################
# STEP: TWO
# TITLE: An Example
# INSTRUCTIONS: Make sure you have the file mbox-short.txt in the same directory as this python file, uncomment
# the code and run it. This is an example to show you the power of regex. This file has a lot in it and this regex
# (regular expression) extracts all the email addresses that are prefixed by the string 'From:'.

# THE CODE:

#import re - this is already done at the top.

#results = []

#hand = open('mbox-short.txt')

#for line in hand:
#    line = line.rstrip()
#    if re.search('^From:', line):
#        print(line + "LINE")

######################################################################################################################


#######################################################################################################################
# STEP: Three
# TITLE: The match function
# INSTRUCTIONS: Change the regExString to match any string that starts with a number
# use the cheatsheet for ideas and also use the website https://regex101.com/ as a tester for your regex
# HINT: the regEx for all lower case is r"[a-z]" and for numbers it is similar and you need the brackets
# Notes: Match is used for looking in the beginning of strings for matches. The next exercise involves
# the search function, which is used to find patterns in the middle of a string, rather than the beginning
# THE CODE:

#inputString = r"From: alexmac2010@gmail.com"
#regExString = r"^From:"
#inputStringFails = "From alexmac2010@gmail.com I am missing the : in From"

#m = re.match(regExString, inputString)

#if m is not None: # m is a match object
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
#inputString = r"2From: alexmac2010@gmail.com
#regExString = r"[0-9]"

######################################################################################################################


#######################################################################################################################
# STEP: four
# TITLE: The search function vs. the match function
# INSTRUCTIONS: swap the search function for the match function and notice how they work differently
# THE CODE:

#inputString = r"From: alexmac2010@gmail.com"
#regExString = r'gmail'

#m = re.search(regExString, inputString)
#m = re.match(regExString, inputString)

#if m is not None: # m is a match object
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
#match() checks from the beginning of the string
#search() checks the entire string for the pattern. Search() evaluates a string from left to right

######################################################################################################################


#######################################################################################################################
# STEP: five
# TITLE: flags for most regex functions
# INSTRUCTIONS: Use a flag to ignore case
# HINT: re.search(pattern, string, flags)
#  and the flag is re.I or re.IGNORECASE
# THE CODE:

#inputString = r"From: alexmac2010@gmail.com"
#regExString = r'GMAIL'

#m = re.search(regExString, inputString)

#if m is not None:
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
# m = re.search(regExString, inputString, re.IGNORECASE)

######################################################################################################################

#######################################################################################################################
# STEP: six
# TITLE: match more than one string
# INSTRUCTIONS: Match more than one string. Change the regular expression to return a match object
# if any of the following strings are matched: "but", "hat", "hit", "hut"
#
# THE CODE:

#inputString = 'He bit me! Oh and he is a bat!'
#regExString = r'bat|bet|bit'

#m = re.search(regExString, inputString)

#if m is not None:
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
#regExString = r'bat|bet|bit|but|hat|hit|hut'
#possible answer could also be [bh][aiu]t

######################################################################################################################

#######################################################################################################################
# STEP: seven
# TITLE: Create a regular expression exercise
# INSTRUCTIONS: Match any pair of words separated by a single space, that is,
# first and last names. Allow for hypens
# HINT: use cheatsheet! Use google. Also, there is more than one regex that will work.
# THE CODE:

inputString = r'Helaine McFerron' #Should pass
inputStringTwo = r'Mary-Jo Harris'
inputStringFails = r'alexmac2010@gmail.com' #should fail

#regExString = r'YOU CREATE THE REGEX'

m = re.search(regExString, inputStringTwo)

if m is not None:
    print(m.group())
    print(type(m))
else:
    print('m is None, so no match was found')


#Answer
#Possible answers
#regExString = r'\S+\s\S+'
#regExString = r'[A-Za-z-]+ [A-Za-z-]+'
######################################################################################################################





