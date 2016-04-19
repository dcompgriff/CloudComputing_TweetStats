#!/usr/bin/env python

from __future__ import print_function
import os
import sys


# os.environ['SPARKHOME'] = '/opt/spark-1.6.1'
# sys.path.append('/opt/spark-1.6.1/python')
# sys.path.append('/opt/spark-1.6.1/python/lib/py4j-0.9-src.zip')



import sys
from pyspark import SparkContext, SparkConf

#Create the SparkContext. The interactive shell does this for you, while pycharm doesn't.
# conf = SparkConf().setAppName('problem1').setMaster('local')
# sc = SparkContext()

if __name__ == "__main__":
  # if len(sys.argv) < 2:
  #   print("enter a filename")
  #   sys.exit(1)

  #sc = SparkContext(appName="avgTweetLength")

  conf = SparkConf().setAppName('problem1').setMaster('local')
  sc = SparkContext()

  #Change to the hadoop file dir on the instance.
  ngrams = sc.textFile('../input/ngrams/googlebooks-eng-all-1gram-20120701-x', )

  #1) Map each line to a tuple as (<year>, <ngram>).
  yearNGramTuples = ngrams.map(lambda line: (line.split('\t')[1], line.split('\t')[0]))
  #2) Use the 'groupByKey()' function to group all ngrams for a year.
  groupedYearNGramTuples = yearNGramTuples.groupByKey()
  #3) Map each (<year>, <ngram data>) tuple to (<year>, len(set(<ngram data>)))
  yearNGramCountTuples = groupedYearNGramTuples.map(lambda tup: (tup[0], len(set(tup[1]))))
  #4) Collect each (<year>, <# distinct ngrams>) tuple for the year.
  finalYearNGramTuples = yearNGramCountTuples.sortByKey()

  # Save to your local HDFS folder
  finalYearNGramTuples.saveAsTextFile("problem1")

  sc.stop()




















