# -*- coding: utf-8 -*-
"""
Created on Tue May 12 09:40:25 2020

@author: chris
"""



from easydict import EasyDict as edict


__C                           = edict()
# Consumers can get config by: from config import cfg

cfg                           = __C

# General options
__C.GENERAL                    = edict()

# Directories
__C.GENERAL.FEATURE            = "TEMPLATE"
__C.GENERAL.LOGFILE            = "../learn_log"
__C.GENERAL.RESULTS_DIR        = "../Results"

# Reporting
__C.GENERAL.ITERATIONCAP       = 20

# Thresholds
__C.GENERAL.TRAINACCTHRESH     = 85
__C.GENERAL.TESTACCTHRESH      = 90
__C.GENERAL.PROBMINTHRESH      = 0.001
__C.GENERAL.PROBMAXTHRESH      = 0.5

# Spectrum options
__C.SPECTRUMS                  = edict()

# Values
__C.SPECTRUMS.NOTE_DIR         = "./notes"
__C.SPECTRUMS.RGB_FILE         = "_RGB.bmp"
__C.SPECTRUMS.IR_FILE          = "_IR.bmp"
__C.SPECTRUMS.HYPSPEC_FILE     = "_HS.bmp"
__C.SPECTRUMS.LASPROF_FILE     = "_LP.bmp"
__C.SPECTRUMS.CHOICES          = ['Red', 'Green', 'Blue', 'InfraRed', 
                                  'HyperSpec1', 'HyperSpec2', 'LaserProfile']

# Method options
__C.METHODS                    = edict()

# Values
__C.METHODS.MODEL_DIR          = "./models"
__C.METHODS.HIST_DIR           = "/hist"
__C.METHODS.BIN_DIR            = "/binary"
__C.METHODS.FILTER_DIR         = "/filter"
__C.METHODS.CNN_DIR            = "/cnn"
__C.METHODS.FOURIER_DIR        = "/fourier"
__C.METHODS.COSINE_DIR         = "/cosine"
__C.METHODS.OCR_DIR            = "/ocr"
__C.METHODS.CHOICES            = ['Histogram', 'Binary', 'Filter', 'DeepCNN',
                                  'Fourier', 'CosineTrans', 'OCR']

# Feature options
__C.FEATURES                   = edict()
__C.FEATURES.FEDSEAL           = "FederalSeal"
