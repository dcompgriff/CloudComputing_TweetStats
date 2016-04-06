#!/usr/bin/env python
import sys

sum = 0
count = 0
currentTweeter = None

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)

    #Should be SUM_ or CNT_
    valKind = val[:4]
    valNum = val[4:]

    if currentTweeter != key:
        if currentTweeter:
            #If the currentTweeter isn't None, then new tweeter. Print out current tweeter values.
            try:
                #Prevent divide by zero error.
                if count != 0:
                    #Print out the current tweeter and their average tweet length.
                    print '%s\t%s' % (currentTweeter, sum/float(count))
            except:
                sys.stderr.write('Error printing tweet length averages in stage2 reduce.')
            if valKind == 'SUM_':
                sum = long(valNum)
            elif valKind == 'CNT_':
                count = long(valNum)
        currentTweeter = key
    else:
        if valKind == 'SUM_':
            sum = long(valNum)
        elif valKind == 'CNT_':
            count = long(valNum)

# Print out the current tweeter and their average tweet length.
print '%s\t%s' % (currentTweeter, sum / float(count))