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
    当n比较小的时候 由于复杂度前面都有常数项 因此 归并有时比插入排序满 可在此处进行优化
    自底向上的归并排序 由于没有用到数组下标 因此可以用于链表排序O(n*logn)
\-快速排序
    选定元素挪到正确位置,挪动的过程也是分离大于选定元素 和 小于选定元素的过程
    递归选定元素两侧的数组进行快排



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


def insertionSort4Ms(arr, l, r):
    for i in range(l, r+1):
        j = i
        temp = arr[i]
        while((j > l) and (arr[j-1] > temp)):
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return

# 递归的使用归并排序arr[l...r]
def __mergeSort(arr, l, r):
    # if l >= r:
    #     return
    # 此处优化 在n比较小时 调用插入排序
    if (r-l) <= 15:
        insertionSort4Ms(arr, l, r)
        return
    mid = int((l+r) / 2)
    __mergeSort(arr, l, mid)
    __mergeSort(arr, mid+1, r)
    # 若有序 无需再合并了
    if (arr[mid] > arr[mid+1]):
        __merge(arr, l, mid, r)


def mergeSort(arr, n):
    # 表示私有
    __mergeSort(arr, 0, n-1)


# 自底向上归并排序(由于没有用到数组下标 因此可以用于链表排序)
def mergeSortBU(arr, n):
    size = 1
    while (size <= n):
        i = 0
        while (i + size < n):
            __merge(arr, i, i+size-1, min(i+size+size-1, n-1))
            i += (size + size)
        size += size


# 对arr[l...r]进行partition
def __partition(arr, l, r):
    temp = arr[l]
    j = l
    for i in range(l+1, r+1):
        if (temp > arr[i]):
            swap(arr, j+1, i)
            j+=1
    swap(arr, j, l)
    return j


# 对arr[l...r]进行快速排序
def __quickSort(arr, l, r):
    if (l>=r):
        return  # 别忘了这个啊 要不然死循环了
    p = __partition(arr, l, r)
    __quickSort(arr, l, p-1)
    __quickSort(arr, p+1, r)

# 快速排序
def quickSort(arr, n):
    __quickSort(arr, 0, n-1)





if __name__ == '__main__':
    n = 1000000
    start = 0
    end = 1000000
    # arr = genNearlyOrderArray(n, swapTimes=100)
    arr = genRandomArray(n, start, end)
    arr2 = arr[:]
    arr3 = arr[:]
    testSort(mergeSort, arr, n)
    testSort(quickSort, arr2, n)