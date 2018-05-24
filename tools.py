#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tools.py
# @Author: 投笔从容
# @Date  : 2018/5/24
# @Desc  : 排序测试辅助工具
import random
import numpy as np
import datetime

def genNearlyOrderArray(n, swapTimes):
    arr = list(range(n))
    for i in range(swapTimes):
        x = random.randint(0, n)
        y = random.randint(0, n)
        swap(arr, x, y)
    return arr


def genRandomArray(n, start=0, end=10000):
    return np.random.randint(start, end, size=n)


def aTestSort(sortName, arr, n):
    t_start = datetime.datetime.now()
    sortName(arr, n)
    t_end = datetime.datetime.now()  # 记录函数结束时间)
    long = (t_end - t_start).total_seconds()
    if isSorted(arr, n):
        print("sortName: %s, time: %f s" % (sortName.__name__, long))
    else:
        print('Sort ERROR!')


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def isSorted(arr, n):
    for i in range(n - 1):
        if (arr[i] > arr[i + 1]):
            return False
    return True