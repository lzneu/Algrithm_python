#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sorting_basic.py
# @Author: 投笔从容
# @Date  : 2018/5/21
# @Desc  : 排序基础

'''
基础排序笔记：
|-为什么要学习O(n^2)的排序算法
    基础
    编码简单易于实现
    在一些特殊的情况下 简单的排序算法更有效
    简单的排序思想衍生出复杂的排序算法
    作为子过程 改进更复杂的排序算法
|-选择排序
    两层循环必须完全执行完成o(n^2)
|-插入排序
    在近乎有序的数据中 排序速度很快 甚至快于O(n*logn)排序算法
    当完全有序时 复杂度为O(n)
|-冒泡排序
|-希尔排序
    插入排序的升级
    逐步减小增量
    复杂度O(n^1.5)
    由于是一种跳跃式的排序 希尔排序不稳定



'''

import datetime
import random
import time


# 生成一个近乎有序的数组
def genNearlyOrderArray(n, swapTimes):
    arr = list(range(n))
    for i in range(swapTimes):
        x = random.randint(0, n)
        y = random.randint(0, n)
        swap(arr, x, y)
    return arr


def genRandomArray(n, start=0, end=10000):
    return random.sample(range(start, end), n)


def testSort(sortName, arr, n):
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


def selectonSort(arr, n):
    for i in range(n):
        # 寻找[i, n)区间里面的最小值
        minIndex = i
        for j in range(i + 1, n):
            if (arr[j] < arr[minIndex]):
                swap(arr, minIndex, j)


def insertionSort(arr, n):
    for i in range(1, n):
        # 寻找arr[i]合适的插入位置
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            swap(arr, j, j - 1)
            j -= 1


def insertionSort2(arr, n):
    for i in range(1, n):
        # 寻找arr[i]合适的插入位置
        j = i
        temp = arr[i]
        while j > 0 and arr[j - 1] > temp:
            # 副本存储代替每次交换
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp


def bubbleSort(arr, n):
    # 设一个标志位 如果没有数据交换 说明排序完成
    flag = True
    for i in range(n):
        if flag == False:
            break
        flag = False
        ite = list(range(i, n))
        ite.reverse()
        for j in ite:
            if (arr[j] < arr[j - 1]):
                swap(arr, j, j - 1)
                flag = True


def shellSort(arr, n):
    increment = n
    while (increment > 1):
        increment = increment // 3 + 1
        for i in range(increment, n):
            if (arr[i] < arr[i - increment]):
                # 将 arr[i]插入有序增量子表
                temp = arr[i]
                j = i - increment
                while (j >= 0 and arr[j] > temp):
                    arr[j + increment] = arr[j]
                    j -= increment
                arr[j + increment] = temp
    return arr


if __name__ == '__main__':
    n = 100000
    start = 0
    end = 100000
    # arr = genNearlyOrderArray(n, swapTimes=100)
    arr = genRandomArray(n, start, end)
    arr2 = arr[:]
    arr3 = arr[:]
    testSort(shellSort, arr, n)
    testSort(insertionSort, arr2, n)
    testSort(insertionSort2, arr3, n)
