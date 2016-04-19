#!/usr/bin/env python
import sys

total = 0
hasLocation = 0

for line in sys.stdin:
    # Each key value pair from the map phase is output on a new
    (key, val) = line.strip().split('\t', 1)
    hasLocation = hasLocation + long(key)
    total = total + long(val)

print hasLocation, float(hasLocation) / float(total)
