#!/usr/bin/env python

import sys
import string
import json

tweeterDict = {'COUNT': long(0), 'SUM': long(0)}

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

    #Don't include prez ono in average.
    if userName == 'PrezOno':
        continue

    #Add tweet length to sum key, and increment the count key.
    tweeterDict['COUNT'] = tweeterDict['COUNT']  + 1
    tweeterDict['SUM'] = tweeterDict['SUM'] + len(userTweet.encode('ascii', 'ignore'))

# Print each tweeter's
for key in tweeterDict.keys():
    print '%s\t%s' % (key, tweeterDict[key])
