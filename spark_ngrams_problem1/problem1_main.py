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
'''
How to run: spark-submit --master yarn-client avgTweetLength.py hdfs://hadoop2-0-0/data/1gram
'''
if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("enter a filename")
    sys.exit(1)
  filename = sys.argv[1]

  sc = SparkContext(appName='DGproblem1')
  ngrams = sc.textFile(filename, )

  #1) Map each line to a tuple as (<ngram>, <year>).
  nGramYearTuples = ngrams.map(lambda line: (line.split('\t')[0], line.split('\t')[1]))
  #2) Reduce each ngram to a tuple of (<ngram>, <years list>). This gets rid of multiple ngrams for the same year.
  nGramYearListTuples = nGramYearTuples.reduceByKey(lambda vs, v2: vs + '\t' + v2)
  #3) Flatmap each ngram year list tuple to (<year>, 1) tuples.
  yearnGramTuples = nGramYearListTuples.flatMap(lambda item: [(year, 1) for year in set(item[1].split('\t'))])
  #4) Reduce by key to get a sum of distinct ngrams for each year.
  sumDistinctNGrams = yearnGramTuples.reduceByKey(lambda vs, v2: long(vs) + long(v2))
  #5) Sort by year.
  sumDistinctNGrams = sumDistinctNGrams.sortByKey()

  sumDistinctNGrams.saveAsTextFile("problem1_run2")

  sc.stop()



















