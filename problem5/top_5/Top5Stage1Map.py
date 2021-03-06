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
        continue
    #Get the user object.
    userName = tweet['user']['screen_name']
    userTweet = tweet['text']

    if userName + '_CNT' in tweeterDict.keys() or userName + '_SUM' in tweeterDict.keys():
        #Increment tweeter tweet number.
        tweeterDict[userName.encode('ascii', 'ignore') + '_CNT'] += 1
        tweeterDict[userName.encode('ascii', 'ignore') + '_SUM'] += len(userTweet.encode('ascii', 'ignore'))
    else:
        #Create new tweeter key for the user.
        tweeterDict[userName.encode('ascii', 'ignore') + '_CNT'] = 1
        tweeterDict[userName.encode('ascii', 'ignore') + '_SUM'] = len(userTweet.encode('ascii', 'ignore'))

# Print each tweeter's
for key in tweeterDict.keys():
    print '%s\t%s' % (key, tweeterDict[key])

























