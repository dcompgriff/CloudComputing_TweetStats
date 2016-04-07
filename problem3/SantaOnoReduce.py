import sys

for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)
    #Pass sorted data through the reduce phase.
    print '%s\t%s' % (val, key)