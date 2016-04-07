import sys

batch = []
for line in sys.stdin:
    (key, val) = line.strip().split('\t', 1)

    #Batch the processing to potentially increase speed since i/o is potentially slow.
    if len(batch) < 1000:
        batch.append((val, key))
    else:
        for tup in batch:
            print '%s\t%s' % (tup[0], tup[1])
        batch = []

#There might be some data left in the batch buffer when the last line
#is read from stdin, so flush the batch buffer.
for tup in batch:
    print '%s\t%s' % (tup[0], tup[1])



