import csv
from scipy.io.wavfile import write
import numpy as np
import math
import pandas as pd

samplerate = 256

class mindDataObj:
    def __init__(self, timestamp, alpha, beta, gamma, theta, delta):
        self.timestamp = timestamp
        self.alpha = alpha
        self.beta = beta
        self.delta = delta
        self.theta = theta
        self.gamma = gamma

mindData = []
rawData = []

error_count = 0

with open('sleepData.csv') as csv_file:
    lastGood = 0
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        
        if line_count == 0:
            mindData.append(["timestamp","alpha","beta","delta","theta","gamma"])
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            try:
                lastGood = float(row[22])
                rawData.append(lastGood) 
            except:
                rawData.append(lastGood)
                error_count +=1
            if line_count % 1024 == 0:
                if row[10] == "" or row[10] == " ''":
                    row[10] = 0
                if row[14] == "" or row[10] == " ''":
                    row[14] = 0
                if row[18] == "" or row[10] == " ''":
                    row[18] = 0
                if row[6] == "" or row[10] == " ''":
                    row[6] = 0
                if row[2] == "" or row[10] == " ''":
                    row[2] = 0
                a= float(row[10])
                b= float(row[14])
                d= float(row[2])
                t= float(row[6])
                g= float(row[18])

                #compute relative brainwaves
                alpha = math.pow(10,a)/(math.pow(10,b)+math.pow(10,d)+math.pow(10,t)+math.pow(10,g))
                beta = math.pow(10,b)/(math.pow(10,b)+math.pow(10,d)+math.pow(10,t)+math.pow(10,g))
                delta = math.pow(10,d)/(math.pow(10,b)+math.pow(10,d)+math.pow(10,t)+math.pow(10,g))
                theta = math.pow(10,t)/(math.pow(10,b)+math.pow(10,d)+math.pow(10,t)+math.pow(10,g))
                gamma = math.pow(10,g)/(math.pow(10,b)+math.pow(10,d)+math.pow(10,t)+math.pow(10,g))
                mindData.append([row[0],alpha,beta,delta,theta,gamma])
            line_count += 1
            
    print("row count =", line_count)
    print("error count =", error_count)
    print("mindData Count =", len(mindData))
    
    df = pd.DataFrame(mindData)
    df.to_csv('relativeBrainwaves.csv', index=False, header=False)

    line_count = 0
    for x in rawData:
        if math.isnan(x):
            rawData[line_count] = 0
        line_count += 1

    rawData = np.interp(rawData, (min(rawData), max(rawData)), (-1, 1))
    nparray = np.array(rawData, dtype=np.float32)
    #scaled = np.int16(rawData/np.max(np.abs(rawData)) * 32767)
    write("Raw.wav", samplerate, nparray)
