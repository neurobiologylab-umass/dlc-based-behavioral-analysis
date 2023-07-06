"""
Movement Scorer Script
Author credit: Jingyi Xu

This script performs movement scoring on a set of data files. It calculates distances 
between points in each file and generates a score based on these distances. 
The scores are then saved in separate CSV files for each input file.
"""
from math import sqrt
import os
import sys;
import csv;
import numpy as np;
import statistics
from math import *;

dataPath = sys.argv
print(dataPath[1])

directory = dataPath[1]

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file):
        print(filename)

    with open(str(file), newline='') as f:
        print("Opened: " + file)
        reader = csv.reader(f)
        file = list(reader)

    jointData = []
    linenum = 0
    dataStartIdx = 0
    for row in file:
        cleanRow = [i for i in row if i != ""]
        if (linenum == 2):
            for i in range(0, len(row)):
                if (row[i] != "x"):
                    dataStartIdx += 1
                else:
                    break
        if (len(cleanRow) > dataStartIdx and linenum > 2):
            for i in range(dataStartIdx, len(cleanRow)):
                cleanRow[i]=float(cleanRow[i])
            jointData.append(cleanRow)
        linenum += 1

    distances = []
    if (len(jointData) > 0):
        for row in jointData:
            distance = 0.0
            thisPair = [str(row[dataStartIdx-2]) + "/" + str(row[dataStartIdx-1])]
            for i in range(dataStartIdx+2, len(row), 2):
                distance = distance + sqrt(pow(row[i]-row[i-2], 2) + pow(row[i+1]-row[i-1], 2))
                thisPair.append(str(distance))
            distances.append(thisPair)
        justDists = [float(img[-1]) for img in distances]
        maxDist = max(justDists)
        minDist = min(justDists)
        medianDist = statistics.median(justDists)
        maximum = ["Max: ", str(maxDist)]
        minimum = ["Min: ", str(minDist)]
        median = ["Median: ", str(medianDist)]
        maxMinRatio = ["MaxMinRatio: ", str(((maxDist-minDist)*100)/minDist)]
        maxMedianRatio = ["MaxMedianRatio: ", str(((maxDist-medianDist)*100)/medianDist)]
        distances.append(maximum)
        distances.append(minimum)
        distances.append(median)
        distances.append(maxMinRatio)
        distances.append(maxMedianRatio)

        with open('Score' + filename + '.csv', 'w') as result:
            write = csv.writer(result)
            write.writerows(distances)

        print("Done, results are in: Score" + filename + ".csv, note rerunning will overwrite that file.")




