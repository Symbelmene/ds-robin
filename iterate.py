# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:48:57 2020

@author: chris
"""

import methods
import numpy as np
from config import cfg
from numpy.random import choice

def iterateMSP(df):
    # Choose MSP
    index = np.array(range(df.count()[0]))
    print(len(index))
    weights = np.array(df['Current Probability'])
    print(len(weights))
    mspIndex = choice(index, p=weights)
    mspRow = df.iloc[mspIndex]
    spectrumType = mspRow['Spectrum']
    methodType = mspRow['Method']
    currProb = mspRow['Current Probability']
    
    print("MSP Selected - {}: {} {} with probability {}".
          format(mspIndex, spectrumType, methodType, round(currProb, 4)))
    
    # Load Model
    currMethod = methods.selectMethod(methodType)
    
    # Run MSP
    trainAcc, testAcc = currMethod(0, 0)

    # Update score
    trainAccThresh = cfg.GENERAL.TRAINACCTHRESH
    testAccThresh = cfg.GENERAL.TESTACCTHRESH
    
    trainScore = trainAcc - trainAccThresh
    testScore = testAcc - testAccThresh
    totalScore = trainScore + testScore
    
    print("MSP Selected - {}: {} {} with probability {}".
          format(mspIndex, spectrumType, methodType, round(currProb, 4)))    
    print("  Train Accuracy = {}%\n  Test Accuracy  = {}%\n  Overall Score  = {}"
          .format(round(trainAcc, 2), round(testAcc, 2), round(totalScore, 2)))
    return mspIndex, totalScore

def updateProbabilities(df, iteration):
    # Update probabilities based on scores
    for i, row in df.iterrows():
        if row['Score'] != 0:
            newProb = df.at[i, 'Current Probability'] * (1 + (row['Score'] / 100))
            df.at[i,'Current Probability'] = newProb
            df.at[i, 'Score'] = 0
            
    # Reduce probabilities to sum to one by dividing by column sum
    sumValue = df['Current Probability'].sum()
    df['Current Probability'] = df['Current Probability'].map(lambda p : p / sumValue)
    if iteration % cfg.GENERAL.ITERATIONCAP == 0:
        df['{} Probability'.format(iteration)] = df['Current Probability']
    return df

def checkThresholds(df):
    probMaxThresh = cfg.GENERAL.PROBMAXTHRESH
    probMinThresh = cfg.GENERAL.PROBMINTHRESH
    for idx, row in df.iterrows():
        if row['Current Probability'] > probMaxThresh:
            print(row['Current Probability'])
            df = df.drop(df.index[[idx]]).reset_index(drop=True)
        if row['Current Probability'] < probMinThresh:
            df = df.drop(df.index[[idx]]).reset_index(drop=True)
    
    # Reduce probabilities to sum to one by dividing by column sum
    sumValue = df['Current Probability'].sum()
    df['Current Probability'] = df['Current Probability'].map(lambda p : p / sumValue)        
    return df