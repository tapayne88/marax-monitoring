#! /usr/bin/env python3

import fileinput
from maraxparser import createTimeBuckets, averageExchangerTemp
import numpy as np
import matplotlib.pyplot as plt

secondsPerBucket = 60

timeBuckets = createTimeBuckets(secondsPerBucket, fileinput.input())
exchangerTempAverages = list(map(averageExchangerTemp, timeBuckets))

print(exchangerTempAverages)

lastIndex = len(exchangerTempAverages) - 1
xy = (lastIndex - 1, exchangerTempAverages[lastIndex])
lastPlot = {
    'xy': xy,
    'title': str(round(xy[1], 1)) + '°C',
    'xytext': (xy[0] + 1.1, xy[1] + 1.1)
}

plt.plot(exchangerTempAverages)
plt.axis([0, 5, 0, 150])
plt.annotate(lastPlot['title'], xy=lastPlot['xy'], xytext=lastPlot['xytext'])
plt.savefig("figure1")
