#!/usr/bin/env python
import sys

totalTweets = 0
currentTweeter = None

for line in sys.stdin:
    #Each key value pair from the map phase is output on a new
    #line, with a tab delimiting the key and value. So, read the
    #line, and parse our the key and value.
    (key, val) = line.strip().split('\t', 1)

    if currentTweeter != key:
        if currentTweeter:
            #If the currentTweeter isn't None, then new tweeter
            # key, so output final previous tweeter uname and tweet count.
            print '%s\t%s' % (currentTweeter, totalTweets)
            totalTweets = val
        currentTweeter = key
    else:
        try:
            #Increment the total number of tweets for a user.
            totalTweets += int(val)
        except:
            continue

#Output the final tweeter and their number of tweets.
print '%s\t%s' % (currentTweeter, totalTweets)