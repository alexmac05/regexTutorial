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

#inputString = r'Helaine McFerron' #Should pass
#inputStringTwo = r'Mary-Jo Harris'
#inputStringFails = r'alexmac2010@gmail.com' #should fail

#regExString = r'YOU CREATE THE REGEX'

#m = re.search(regExString, inputStringTwo)

#if m is not None:
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
#Possible answers
#regExString = r'\S+\s\S+'
#regExString = r'[A-Za-z-]+ [A-Za-z-]+'
######################################################################################################################


#######################################################################################################################
# STEP: eight
# TITLE: Create a regular expression exercise
# INSTRUCTIONS: Match any word and single letter separated by a comma and single space, as in last name, first
# initial. Should pass: Garcia, B.
# HINT: use cheatsheet! Use google. Also, there is more than one regex that will work.
# THE CODE:

#inputString = r'Garcia, B. ' #Should pass
#inputStringFails = r'alexmac2010@gmail.com' #should fail

#regExString = r'YOU CREATE THE REGEX'

#m = re.search(regExString, inputString)

#if m is not None:
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


#Answer
#Possible answers
#regExString = r'[A-Za-z-]+, [A-Za-z]'
######################################################################################################################


#######################################################################################################################
# STEP: nine
# TITLE: Demo - matching any single character with a dot .
# INSTRUCTIONS: Play with the following example, until it is clear that a dot cannot match a \n
# or a non-character (empty string) but it can match other characters. Also, what if you were looking
# for 3.14. Understand all of these topics using this demo
# Homework. To understand more about r'' you can read
# http://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-in-python-and-what-are-raw-string-l

# THE CODE:

#inputString1 = r'bend'
#regExString1 = r'.end'
#inputString2 = r'end'
#inputString3 = '\nend' # do not use r'' with the newline character
#print(inputString3) #notice it has a newline character '\n'
#inputString4 = r"The end."

#regExString2 = '3\.14'
#inputString5 = '3.14'
#inputString6 = '3P14'

#m = re.match(regExString1, inputString3, re.DOTALL) #the re.DOTALL adds newlines to the list of excepted chars with .
#m = re.match(regExString1, inputString1)
#m = re.search(regExString1, inputString4)
#m = re.match(regExString2, inputString6)


#if m is not None:
#    print(m.group())
#    print(type(m))
#else:
#    print('m is None, so no match was found')


######################################################################################################################


#######################################################################################################################
# STEP: ten
# TITLE: Create a regular expression exercise
# INSTRUCTIONS: Match simple web domain names that begin with "www." and end with a ".com" suffix;
# for example, www.yahoo.com. Extra credit: If your regex also supports other high-level domain names,
# such as .edu, .net, (for example www.foothill.edu)


######################################################################################################################


#######################################################################################################################
# STEP: eleven
# TITLE: Create a regular expression exercise
# INSTRUCTIONS: 


######################################################################################################################

