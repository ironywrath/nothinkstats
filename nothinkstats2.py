import bisect
import copy
import logging
import math
import random
import re

from collections import Counter
from operator import itemgetter

import numpy as np
#import pandas

#import scipy

from io import open

ROOT2 = math.sqrt(2)

def RenderParetoCdf(xmin, alpha, low, high, n=50):
    if low<xmin:
        low = xmin
    xs = np.linspace(low, high, n)
    ps = 1 - (xs / xmin) ** -alpha

    return xs,ps

class ParetoCdfTest:

    xs = list()

    def LinspaceTest(self, low, high, n):
        return np.linspace(low, high, n)

    def ParetoCdfTest1(self, xmin, alpha):
        return self.xs/xmin

    def ParetoCdfTest2(self, xmin, alpha):
        return (self.xs/xmin)**alpha

    def ParetoCdfTest3(self, xmin, alpha):
        return (self.xs/xmin)**-alpha

    def ParetoCdfTest4(self, xmin, alpha):
        return 1- (self.xs/xmin)**-alpha

    def __init__(self):
        return

def RenderExpoCdf(lam, low, high, n=100):
    xs = np.linspace(low, high, n)
    ps = 1 - np.exp(-lam*xs)
    return xs, ps


