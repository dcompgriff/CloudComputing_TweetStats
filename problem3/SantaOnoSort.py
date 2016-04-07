#!/usr/bin/env python
'''
Note that this program isn't mapreduce bc the size of the data input is around 50 Mb. If the data was larger
than could be held in memory, then the data would have to be sorted using the mapreduce sorting design
pattern.
'''
import sys

data = []
#Read in all data.
for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    data.append((key, val))

#Sort all data.
data = sorted(data, key=lambda item: float(item[1]))

#Do quick linear search for 'PrezOno'
mindex = -1
for i in range(0, len(data)):
    if data[i][0] == 'PrezOno':
        mindex = i
        break;

#Print out all results.
print('Total Number of Tweeters: ' + str(len(data)))
print('PrezOno Index: ' + str(mindex))
print('PrezOno Stats: ' + str(data[mindex]))


