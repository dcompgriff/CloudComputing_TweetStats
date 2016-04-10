#!/usr/bin/env python
import sys

mapKey = ""
maxLength = 0
maxKey = ""
mapVal = ""

for line in sys.stdin:
    # Each key value pair from the map phase is output on a new
    (key, val) = line.strip().split('\t', 1)

    # If the key shows up again, concatenate the results
    if mapKey == key:
        mapVal += long(val)
    # If the key is done showing up, set up the next one
    else:
        mapKey = key
        mapVal = long(val)

    if maxLength > mapVal:
        # Move on...
        continue
    else:
        maxLength = mapVal
        maxKey = key

print '%s\t%s' % (maxKey, maxLength)
