from __future__ import print_function

import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import tkinter as TK

class _Brewer(object):

    color_iter = None

    colors = ['#f7fbff', '#deebf7', '#c6dbef',
              '#9ecae1', '#6baed6', '#4292c6',
              '#2171b5','#08519c','#08306b'][::-1]

    which_colors = [[],
                    [1],
                    [1, 3],
                    [0, 2, 4],
                    [0, 2, 4, 6],
                    [0, 2, 3, 5, 6],
                    [0, 2, 3, 4, 5, 6],
                    [0, 1, 2, 3, 4, 5, 6],
                    [0, 1, 2, 3, 4, 5, 6, 7],
                    [0, 1, 2, 3, 4, 5, 6, 7, 8],
                    ]

    current_figure = None

    #@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。

    @classmethod
    def Colors(cls):
        return cls.colors

    @classmethod
    def ColorGenerator(cls, num):

        for i in cls.which_colors[num]:
            yield  cls.colors[i] #yield就是 return 返回一个值，并且记住这个返回的位置，下次迭代就从这个位置后(下一行)开始。
        raise StopIteration('Ran out of color in _Brewer.')

    @classmethod
    def InitIter(cls, num):
        cls.color_iter = cls.ColorGenerator(num)
        fig = plt.gcf()
        cls.current_figure = fig

    @classmethod
    def ClearIter(cls):
        cls.color_iter = None
        cls.current_figure = None

    @classmethod
    def GetIter(cls, num):

        fig = plt.gcf()
        if fig != cls.current_figure:
            cls.InitIter(num)
            cls.current_figure = fig

        if cls.color_iter is None:
            cls.InitIter(num)

        return cls.color_iter

def PrePlot(num=None, rows=None, cols=None):

    if num:
        _Brewer.InitIter(num)

    if rows is None and cols is None:
        return

    if rows is not None and cols is None:
        cols = 1
    if cols is not None and rows is None:
        rows = 1

    size_map = {(1, 1): (8, 6),
                (1, 2): (12, 6),
                (1, 3): (12, 6),
                (1, 4): (12, 5),
                (1, 5): (12, 4),
                (2, 2): (10, 10),
                (2, 3): (16, 10),
                (3, 1): (8, 10),
                (4, 1): (8, 12),
                }

    if (rows, cols) in size_map:
        fig = plt.gcf()
        fig.set_size_inches(*size_map[rows, cols])

    if rows > 1 or cols > 1:
        ax = plt.subplot(rows, cols, 1)
        global SUBPLOT_ROWS, SUBPLOT_COLS
        SUBPLOT_ROWS = rows
        SUBPLOT_COLS = cols
    else:
        ax = plt.gca()

    return ax

def main():
    color_iter = _Brewer.ColorGenerator(7)
    for color in color_iter:
        print(color)

if __name__ == '__main__':
    main()