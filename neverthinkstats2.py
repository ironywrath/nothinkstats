from __future__ import print_function

import csv
import logging
import sys
import numpy as np
import pandas as pd



def ReadmpgData():
    df = pd.read_csv('mpg.csv')
    return df

