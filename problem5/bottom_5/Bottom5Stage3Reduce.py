#!/usr/bin/env python

import sys
import string
import json

top5 = []
for i in range(0,5):
    top5.append(('', 0.0))

for line in sys.stdin:
    #Each tweet exists on a single line. Try to parse string to dict.
    (key, val) = line.strip().split('\t', 1)

    #Pull the tweeter name and average value from the string tuple.
    tweeterName = None
    tweeterAverage = 0
    try:
        tweeterName = val.strip().split(',')[0][2:-1]
        tweeterAverage = val.strip().split(',')[1][1:-1]
    except:
        sys.stderr.write('Error parsing tuple in stage3 reduce.')

    #Append the new tweeter to the list.
    top5.append((tweeterName, float(tweeterAverage)))
    #Sort the list.
    top5 = sorted(top5, key=lambda item: item[1], reverse=False)
    #Remove the smallest average tweeter from the list.
    top5 = top5[:-1]

#Print the final set of top 5.
for tup in top5:
    print '%s\t%s' % (tup[0], str(tup[1]))























