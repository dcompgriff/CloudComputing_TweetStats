#!/usr/bin/env python
import sys

sum = 0
currentTweeter = None

for line in sys.stdin:
    #Each key value pair from the map phase is output on a new
    #line, with a tab delimiting the key and value. So, read the
    #line, and parse our the key and value.
    (key, val) = line.strip().split('\t', 1)

    if currentTweeter != key:
        if currentTweeter:
            #If the currentTweeter isn't None, then new tweeter. Print out current tweeter values.
            try:
                print '%s\t%s' % (currentTweeter, str(sum))
            except:
                sys.stderr.write('Error printing tweet length averages in stage1 reduce.')
            # _CNT should be encountered first, so set the total tweets to val.
        sum = long(val)
        currentTweeter = key
    else:
        try:
            sum += long(val)
        except:
            continue

#Output the final tweeter and their number of tweets.
try:
    print '%s\t%s' % (currentTweeter, str(sum))
except:
    sys.stderr.write('Error printing final tweeter average in stage1 reduce.')

