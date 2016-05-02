import re
#######################################################################################################################
# STEP: ONE
# TITLE: Do you have python working?
# INSTRUCTIONS: uncomment the print statement and run it
# HINT: if you get stuck, you can read this page https://docs.python.org/3/howto/regex.html
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
# HINTS:
# \d Matches any decimal digit, same as [0-9] and \D is the inverse of \d: do not match any numeric digit
# \w Matches any alphanumeric character, same as [A-Za-z0-9_] and \W is the inverse of \w
# (...) Match enclosed regex and save as a subgroup ex: f(oo|u)bar
# EXAMPLES:
# \w+-\d+ Alphanumeric string and number separated by a hyphen
# \d{3}-\d{3}-\d{4} American-format telephone numbers with an area code prefix, as in 800-555-1212.
# The {N} in the above means Match N occurrences of preceding regex

#ANSWER
# pattern = '\w+@\w+\.com'
######################################################################################################################


#######################################################################################################################
# STEP: eleven
# TITLE: demo of findall() and finditer()
# INSTRUCTIONS: Explore the code below to learn about findall() and finditer() so you can do exercise twelve
# NOTES: findall() looks for occurrences of a regex pattern and returns a list. The list will be empty if no
# occurrences are found, but if successful, the list will consist of all matches found
# HINT: https://docs.python.org/3/library/re.html#match-objects
# and https://docs.python.org/3/howto/regex.html
#results = re.findall('car', 'carry the barcardi to the car')
#print(results)

#s = 'This and that. So, what happens here? Does this entire string match? This and that.'
#regex = r'(th\w+) and (th\w+)'
#results = re.findall(regex,s,re.IGNORECASE)
#print(results)

#finditer() is a more memory-friendly alternative to findall()
#returns an iterator instead of a list
#iterator = re.finditer(regex, s, re.IGNORECASE)

#for match in iterator:
#    print(match.span())

#print(s[0:13]) #This part of the string matches
#print(s[69:82])
#print(len(s),  ' is length of the string')

######################################################################################################################

#######################################################################################################################
# STEP: twelve
# TITLE: An Example
# INSTRUCTIONS: Make sure you have the file mbox-short.txt in the same directory as this python file, uncomment
# the code and run it. This is an example to show you the power of regex. This file has a lot in it and this regex
# (regular expression) extracts all the email addresses that are prefixed by the string 'From:'.
# Assignment - change the code so that you collect from this file, all of the domains represented
# domains - from the email address stephen.marquard@uct.ac.za, you should add uct.ac.za to the results list but
# add it only once. Then add media.berkeley.edu only once. Make sure you have a full list of all of hte domains
# where emails were sent FROM in this file
# THE CODE:

#import re - this is already done at the top.

#results = []

#hand = open('mbox-short.txt')

#for line in hand:
#    line = line.rstrip()
#    if re.search('^From:', line):
#        print(line + " LINE")

######################################################################################################################


#More exercises
#1. from the file get timestamps. Sat, 5 Jan 2008 09:12:19 -0500 and then extract day, month, day of week, and time
#2. Extract all timestamps from the file and find out the years. You want to understand what years these emails were sent
#3. Extract from this file any IP addresses. 134.68.220.122 is an example of an IP address
#4. Extract a list of all modified files from the file. And all added files from the file.
