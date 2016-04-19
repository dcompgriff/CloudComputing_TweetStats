

import matplotlib.pyplot as plt
import numpy as np
import os

yearList = []
countList = []


with open('../output/ngrams_output/new_out', 'rb') as f:
    for line in f.readlines():
        tupElems = line.split(',')
        yearList.append(tupElems[0][3:-1])
        countList.append(long(tupElems[1].strip()[:-2]))

xVals = np.arange(0, len(yearList), 1)
plt.bar(xVals, countList)
plt.xticks(xVals, yearList, rotation='vertical')
plt.savefig('./year_count_plot.png')















