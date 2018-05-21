#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sorting_advanced.py
# @Author: 投笔从容
# @Date  : 2018/5/21
# @Desc  : 高级排序

'''
O(n*logn)级别的排序
\-归并排序
    分成log(n)个层级 每个层级进行O(n)排序
    每次归并时 开辟一个新的存储空间作为辅助 因此需要使用O(n)多的空间
    用三个索引进行归并 时间复杂度O(n)


'''


# 生成一个近乎有序的数组
import datetime
import random


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
    for i in range(n-1):
        if(arr[i] > arr[i+1]):
            return False
    return True


# 将arr[l...mid] 和 arr[mid+1...r]两部分合并
def __merge(arr, l, mid, r):
    aux = arr[l: r+1]
    i = l
    j = mid + 1
    for k in range(l, r+1):

        if (i > mid):
            arr[k] = aux[j-l]
            j+=1
        elif (j > r):
            arr[k] = aux[i-l]
            i+=1
        elif (aux[i-l] < aux[j-l]):
            arr[k] = aux[i-l]
            i+=1
        else:
            arr[k] = aux[j-l]
            j+=1




# 递归的使用归并排序arr[l...r]
def __mergeSort(arr, l, r):
    if l >= r:
        return
    mid = int((l+r) / 2)
    __mergeSort(arr, l, mid)
    __mergeSort(arr, mid+1, r)
    __merge(arr, l, mid, r)


def mergeSort(arr, n):
    # 表示私有
    __mergeSort(arr, 0, n-1)





if __name__ == '__main__':
    n = 10000
    start = 0
    end = 10000
    # arr = genNearlyOrderArray(n, swapTimes=100)
    arr = genRandomArray(n, start, end)
    arr2 = arr[:]
    arr3 = arr[:]
    testSort(mergeSort, arr, n)