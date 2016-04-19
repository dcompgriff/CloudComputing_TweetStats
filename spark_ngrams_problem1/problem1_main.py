#!/usr/bin/env python

from __future__ import print_function
import os
import sys


# os.environ['SPARKHOME'] = '/opt/spark-1.6.1'
# sys.path.append('/opt/spark-1.6.1/python')
# sys.path.append('/opt/spark-1.6.1/python/lib/py4j-0.9-src.zip')



import sys, json
from pyspark import SparkContext, SparkConf

#Create the SparkContext. The interactive shell does this for you, while pycharm doesn't.
# conf = SparkConf().setAppName('problem1').setMaster('local')
# sc = SparkContext()



# Given a full tweet object, return the text of the tweet
def getText(line):
  try:
    js = json.loads(line)
    text = js['text'].encode('ascii', 'ignore')
    return [text]
  except Exception as a:
    return []

if __name__ == "__main__":
  # if len(sys.argv) < 2:
  #   print("enter a filename")
  #   sys.exit(1)

  #sc = SparkContext(appName="avgTweetLength")

  conf = SparkConf().setAppName('problem1').setMaster('local')
  sc = SparkContext()

  #tweets = sc.textFile(sys.argv[1],)
  tweets = sc.textFile('../input/part-03212', )

  texts = tweets.flatMap(getText)
  lengths = texts.map(lambda l: len(l))

  # Just show 10 tweet lengths to validate this works
  print(lengths.take(10))
  # Print out the stats
  print(lengths.stats())

  # Save to your local HDFS folder
  lengths.saveAsTextFile("lengths")


  sc.stop()




















