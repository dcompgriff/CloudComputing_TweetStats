#!/usr/bin/env python

import sys

topTweeterName = None
topTweeterTotalTweets = 0

for line in sys.stdin:
    (key, value) = line.strip().split('\t', 1)

    if key != 'TOP_TWEETER':
        sys.stderr.write('Key other than TOP_TWEETER found in stage 2 reduce.')
    #Parse the name and total tweets tuple value out of the value string.
    try:
        tweeterName = value.strip().split(',')[0][2:-1]
        tweeterTotalTweets = value.strip().split(',')[1][1:-1]
    except:
        sys.stderr.write('Error parsing tuple in stage2 reduce.')

    #Update the top tweeter values.
    if int(tweeterTotalTweets) > topTweeterTotalTweets:
        topTweeterName = tweeterName
        topTweeterTotalTweets = int(tweeterTotalTweets)

#Print the final top tweeter name.
print '%s\t%s' % (topTweeterName, topTweeterTotalTweets)












