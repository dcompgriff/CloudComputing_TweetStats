#!/usr/bin/env python

import sys
import string
import json

stringList = []

for line in sys.stdin:
    #Each tweet exists on a single line. Try to parse string to dict.
    (key, val) = line.strip().split('\t', 1)

    #Get the user name from the key.
    keyName = key[:-4]
    #Get the kind, CNT or SUM of the key value pair.
    keyKind = key[-3:]

    #Add the string to a list, and chunk outputs to minimize i/o.
    stringList.append('%s\t%s' % (keyName, keyKind + '_' + val))
    if len(stringList) > 1000:
        for string in stringList:
            print string
        stringList = []

#Print the final set of strings.
for string in stringList:
    print string

























