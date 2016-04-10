#!/usr/bin/env python

import sys
import json

hasLocation = 0
total = 0

for line in sys.stdin:
    # Each tweet exists on a single line. Try to parse string to dict.
    tweet = None
    try:
        tweet = json.loads(line)
    except:
        sys.stderr.write('Error parsing string to dict.')
        continue

    total += 1

    # Get the users locaiton
    userGeolocation = tweet['geo']

    # Does the user have a location?
    if userGeolocation:
        coordinates = userGeolocation['coordinates']

        # Check if the user has a location coordinate
        if coordinates and userGeolocation['type'] == 'Point':
            hasLocation += 1


# Print the totals
print '%s\t%s' % (hasLocation, total)
