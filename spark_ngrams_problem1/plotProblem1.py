

import matplotlib.pyplot as plt
import numpy as np
import os

yearList = []
countList = []


with open('../output/ngrams_output/full_output.txt', 'r') as f:
    for line in f.readlines():
        tupElems = line.split(',')
        yearList.append(tupElems[0][3:-1])
        countList.append(long(tupElems[1].strip()[:-2]))

xVals = np.arange(0, len(yearList), 1)
xTicks = np.arange(0, len(yearList), 4)
yearLabels = np.array(yearList)[xTicks]

fig = plt.gcf()
fig.set_size_inches(30, 10)
#fig.savefig('test2png.png', dpi=100)
plt.bar(xVals, countList, width=1)
plt.xticks(xTicks, yearLabels, rotation='vertical')
plt.show()
#plt.savefig('./year_count_plot.png')















