#! /usr/bin/env python3

import fileinput
from maraxparser import createTimeBuckets, averageExchangerTemp

secondsPerBucket = 60

timeBuckets = createTimeBuckets(secondsPerBucket, fileinput.input())
exchangerTempAverages = list(map(lambda x: averageExchangerTemp(x), timeBuckets))

print(exchangerTempAverages)
