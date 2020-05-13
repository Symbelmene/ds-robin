# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:40:24 2020

@author: chris
"""

import cv2

def loadSpectrumRGB(fileRGB):
    image = cv2.imread(fileRGB, cv2.COLOR_BGR2RGB)
    R = 0
    G = 0
    B = 0
    return R, G, B
    
def loadSpectrumIR(fileIR):
    IR = 0
    return IR
    
def loadSpectrumHS(fileHS):
    HS = 0
    return HS
    
def loadSpectrumLP(fileLP):
    LP = 0
    return LP