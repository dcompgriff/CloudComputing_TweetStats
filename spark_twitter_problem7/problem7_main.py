#!/usr/bin/env python
from __future__ import print_function
import os
import sys

import sys, json
from pyspark import SparkContext, SparkConf

def trim_locations(l):
    fixedKeySize = 2

    coordinates = json.loads(l)['geo']
    if coordinates:
        coordinates = coordinates['coordinates']
        if coordinates:
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
            return (lat + ',' + lon, 1)
    return None

def filter_locations(c):
    return c

def reduce_locations(v1, v2):
    return v1 + v2

def max_locations(x):
    return x[1]

if __name__ == "__main__":
    SparkConf().setAppName('problem7').setMaster('local')
    sc = SparkContext()

    tweets = sc.textFile('../input/part-03212')

    locations = tweets.map(trim_locations) \
        .filter(filter_locations)

    tweetsCount = tweets.count()
    locationsCount = locations.count()

    centroid = locations.reduceByKey(reduce_locations) \
        .max(max_locations)

    percentage = float(locationsCount) / float(tweetsCount)

    f = open('results.txt', 'w')
    f.write("\nCentroid: %s & Percentage: %f\n" % (centroid, percentage))
    f.close()

    sc.stop()
