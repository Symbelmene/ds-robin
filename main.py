# -*- coding: utf-8 -*-
"""
Created on Mon May 11 15:35:48 2020

@author: chris

ds-genesys-beta MAIN FUNCTION

"""


import iterate
import pandas as pd
from config import cfg
import numpy as np

# Disable warnings
pd.options.mode.chained_assignment = None  # default='warn'

# Create list of available spectrums
specList = cfg.SPECTRUMS.CHOICES

# Create list of available methods
methodList = cfg.METHODS.CHOICES

# Create list of possible MSPs
mspList = [(x,y) for x in specList for y in methodList]
print("Found {} possible MSPs".format(len(mspList)))

df = pd.DataFrame(mspList, columns=['Spectrum', 'Method'])
df['Score'] = 0
df['Current Probability'] = 1 / (len(mspList))

probs = np.array(df['Current Probability'])

for it in range(500):
    # Iterate MSP
    mspIndex, score = iterate.iterateMSP(df)
    
    # Update dataframe with score
    df.at[mspIndex, 'Score'] = score
    
    # Update probabilities based on score
    df = iterate.updateProbabilities(df, it)
    
    # Check dataframe for threshold probabilities
    df = iterate.checkThresholds(df)