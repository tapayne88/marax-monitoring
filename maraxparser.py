#! /usr/bin/env python3

from functools import reduce

def createTimeBuckets(secondsPerBucket, lines):
    messagesPerSecond = 2.5

    timeBuckets = [[]]
    bucketTargetSize = messagesPerSecond * secondsPerBucket
    bucketIndex = 0

    for line in lines:
        if (len(timeBuckets[bucketIndex]) == bucketTargetSize):
            bucketIndex = bucketIndex + 1
            timeBuckets.append([])

        timeBuckets[bucketIndex].append(parseTempCSV(line.rstrip()))

    return timeBuckets

def parseTempCSV(temp):
    [
        version,
        steamTemp,
        targetTemp,
        exchangerTemp,
        fastHeating,
        heating
    ] = temp.split(',')

    return {
        "mode": version[0],
        "version": version[1:],
        "steamTemp": int(steamTemp),
        "targetTemp": int(targetTemp),
        "exchangerTemp": int(exchangerTemp),
        "fastHeating": fastHeating,
        "heating": heating == 1
    }

def averageExchangerTemp(bucket):
    noOfReadings = len(bucket)
    total = reduce((lambda x, y: x + y["exchangerTemp"]), bucket, 0)
    return total / noOfReadings
