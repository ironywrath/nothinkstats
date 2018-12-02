from __future__ import print_function

import csv
import sys
import numpy as np
import pandas as pd

def ReadAAPL(filename = 'AAPL.csv'):

    df = pd.read_csv(filename, header=None, skiprows=0)
    return df

def main():
    return

if __name__ == "__main__":
    main()