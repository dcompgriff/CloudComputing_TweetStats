#!/usr/bin/env python

import sys
import json

latLon = {}

for line in sys.stdin:
    # Each tweet exists on a single line. Try to parse string to dict.
    tweet = None
    try:
        tweet = json.loads(line)
    except:
        sys.stderr.write('Error parsing string to dict.')
        continue

    # Get the users locaiton
    userGeolocation = tweet['geo']

    # Does the user have a location?
    if userGeolocation:
        coordinates = userGeolocation['coordinates']

        # Check if the user has a location coordinate
        if coordinates and userGeolocation['type'] == 'Point':
            # Fixed geolocation key size
            # Create a big enough key size
            fixedKeySize = 2

            lat = coordinates[0]
            lon = coordinates[1]

            if lat > 0:
                lat = str(lat)[:fixedKeySize]
            else:
                if lat > 99:
                    lat = str(lat)[:fixedKeySize + 2]
                else:
                    lat = str(lat)[:fixedKeySize + 1]

            if lon > 0:
                lon = str(lon)[:fixedKeySize]
            else:
                if lon < -99:
                    lon = str(lon)[:fixedKeySize + 2]
                else:
                    lon = str(lon)[:fixedKeySize + 1]

            # rounded & trunated [lat,lon] => original coordinates + '.'
            mapKey = lat + ',' + lon

            # If the map key exists, then add the new coordiates to it,
            if mapKey in latLon:
                latLon[mapKey] = latLon[mapKey] + 1
            # else just add the root coordinate
            else:
                latLon[mapKey] = 1


# Print each tweeters location
for key in latLon.keys():
    print '%s\t%s' % (key, latLon[key])
