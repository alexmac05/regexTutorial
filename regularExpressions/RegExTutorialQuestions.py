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

import re

results = []

hand = open('mbox-short.txt')

for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line + "LINE")

    #dictOfEmails = re.findall('From: \S+?@\S+',line)
    #print(dictOfEmails)

    #results.append(dictOfEmails)

#print(results)

######################################################################################################################
