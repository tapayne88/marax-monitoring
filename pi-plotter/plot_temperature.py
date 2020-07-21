import fileinput
from maraxparser import createTimeBuckets, averageExchangerTemps, parseRow, extractExchangerTemps
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image, ImageDraw, ImageFont

useBuckets = False
lines = fileinput.input()

if (useBuckets):
    secondsPerBucket = 60

    timeBuckets = createTimeBuckets(secondsPerBucket, lines)
    exchangerTemps = list(map(averageExchangerTemps, timeBuckets))
else:
    parsedLines = list(map(parseRow, lines))
    exchangerTemps = extractExchangerTemps(parsedLines)

print(exchangerTemps)

lastIndex = len(exchangerTemps) - 1
xy = (lastIndex - 1, exchangerTemps[lastIndex])
lastPlot = {
    'xy': xy,
    'title': str(round(xy[1], 1)) + '°C',
    'xytext': (xy[0] + 1.1, xy[1] + 1.1)
}

plt.plot(exchangerTemps)
plt.axis('off')
plt.autoscale(False)
plt.annotate(lastPlot['title'], xy=lastPlot['xy'], xytext=lastPlot['xytext'])

with io.BytesIO() as file:
    plt.savefig(file)
    file.seek(0)
    img = Image.open(file)
    img.save("figure1.png")
