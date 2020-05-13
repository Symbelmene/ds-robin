# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:40:24 2020

@author: chris
"""

import random

def methodHist(genData, nonData):
    # Placeholder
    trainAcc = 100 # random.randint(50, 100)
    testAcc = 100 # trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodBin(genData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodFilter(imaggenData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodCNN(genData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodFourier(genData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodCosine(genData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100
    return trainAcc, testAcc

def methodOCR(genData, nonData):
    # Placeholder
    trainAcc = random.randint(50, 100)
    testAcc = trainAcc * random.randint(90, 110) / 100    
    return trainAcc, testAcc

methodFunctionList = [methodHist, methodBin, methodFilter, methodCNN,
                      methodFourier, methodCosine, methodOCR]

def selectMethod(methodType):
    if methodType == 'Histogram':
        return methodHist
    elif methodType == 'Binary':
        return methodBin
    elif methodType == 'Filter':
        return methodFilter
    elif methodType == 'DeepCNN':
        return methodCNN
    elif methodType == 'Fourier':
        return methodFourier
    elif methodType == 'CosineTrans':
        return methodCosine
    elif methodType == 'OCR':
        return methodOCR
    else:
        print("ERROR: Method not found!")
        return 0
        