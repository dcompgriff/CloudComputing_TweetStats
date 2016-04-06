#!/usr/bin/env python

import sys
import string
import json

tweeterDict = {}

for line in sys.stdin:
    #Each tweet exists on a single line. Try to parse string to dict.
    tweet = None
    try:
        tweet = json.loads(line)
    except:
        sys.stderr.write('Error parsing string to dict.')
    #Get the user object.
    userName = tweet['user']['screen_name']

    if userName in tweeterDict.keys():
        #Increment tweeter tweet number.
        tweeterDict[userName.encode('ascii', 'ignore')] += 1
    else:
        #Create new tweeter key for the user.
        tweeterDict[userName.encode('ascii', 'ignore')] = 1

# Print each tweeter's
for key in tweeterDict.keys():
    print '%s\t%s' % (key, tweeterDict[key])

























