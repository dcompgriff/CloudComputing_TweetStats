

import matplotlib.pyplot as plt
import numpy as np

yearList = []
countList = []
with open('./problem1/part-00000', 'rb') as f:
    for line in f.readlines():
        tupElems = line.split(',')
        yearList.append(tupElems[0][1:])
        countList.append(int(tupElems[1][:-1]))

with open('./problem1/part-00001', 'rb') as f:
    for line in f.readlines():
        tupElems = line.split(',')
        yearList.append(tupElems[0][1:])
        countList.append(int(tupElems[1][:-1]))

xVals = np.arange(0, len(yearList), 1)
plt.bar(xVals, countList)
plt.set_xticklabels(yearList)
plt.show()















