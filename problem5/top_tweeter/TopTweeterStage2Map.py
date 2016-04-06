#!/usr/bin/env python

import sys
import json

topTweeter = None
topTweeterTotalTweets = 0

for line in sys.stdin:
    (key, value) = line.strip().split('\t', 1)
    if int(value) > topTweeterTotalTweets:
        topTweeterTotalTweets = int(value)
        topTweeter = key

#Print out the final top tweeter for this mapper as 'TOP_TWEETER\t('')'
print '%s\t%s' % ('TOP_TWEETER', str((topTweeter,topTweeterTotalTweets)))






















