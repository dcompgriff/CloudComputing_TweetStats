#!/usr/bin/env python

import sys
import string
import json

top5 = []
for i in range(0,5):
    top5.append(('', 10000))

for line in sys.stdin:
    #Each tweet exists on a single line. Try to parse string to dict.
    (key, val) = line.strip().split('\t', 1)

    if key.strip() == '' or float(val) < 0.000001:
        continue

    #Append the new tweeter to the list.
    top5.append((key, float(val)))
    #Sort the list.
    top5 = sorted(top5, key=lambda item: item[1], reverse=False)
    #Remove the smallest average tweeter from the list.
    top5 = top5[:-1]

#Print the final set of top 5.
for tup in top5:
    print '%s\t%s' % ('BOTTOM_5', str(tup))






















