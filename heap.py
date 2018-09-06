#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : heap.py
# @Author: 投笔从容
# @Date  : 2018/5/23
# @Desc  : 堆 和 堆排序

'''
|—使用堆实现优先队列:
    对于总共N个请求 使用普通数组或者顺序数组 最差情况O(N^2)
    使用堆 O(N*Log N)

|-堆的基本实现
    二叉堆：任何一个子节点都不大于他的父节点
            必须是一棵完全二叉树
            用数组存储二叉堆：
|-shift up
|-shift down
|-基础堆排序
    heapSort1
|-heapify 堆排序
    建堆的过程直接构建 不用挨个元素插入
    新建一个堆的构造函数 , 传入一个数组arr 和 该数组长度n

|-原地堆排序
    堆的索引从数组下标0开始
    无需额外的空间
    parent(i) = (i-1)/2
    left child(i) = 2*i +1
    right child(i) = 2*i +2






'''
import random
from tools import *
import sorting_advanced


class MaxHeap:

    def __init__(self):
        self.__data = [0]
        self.__count = 0

    # 构造函数 给定一个数组创建一个最大堆 时间复杂度O(n)
    def buildHeap(self, arr):
        n = len(arr)
        self.__count = n
        self.__data = [0]
        self.__data.extend(arr)
        for i in range(n // 2):
            index = n // 2 - i
            self.__shiftDown(index)

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    def __swap(self, i, j):
        temp = self.__data[i]
        self.__data[i] = self.__data[j]
        self.__data[j] = temp

    # 最大堆核心辅助函数
    def __shiftUp(self, k):
        while (k > 1) and (self.__data[(k // 2)] < self.__data[k]):
            self.__swap(k // 2, k)
            k = k // 2

    def insert(self, item: object) -> object:
        self.__data.append(item)
        self.__count += 1
        self.__shiftUp(self.__count)

    def __shiftDown(self, k):
        # 判断有无左孩子
        while (2 * k <= self.__count):
            j = 2 * k  # 在此轮循环中 data[k] 与 data[j] 交换位置
            if (j + 1 <= self.__count and self.__data[j + 1] > self.__data[j]):
                j += 1
            if (self.__data[k] >= self.__data[j]):
                break
            self.__swap(k, j)
            k = j

    # 从队中去除堆顶元素 即堆中所存储的最大元素
    def extractMax(self):
        if self.__count <= 0:
            raise IndexError
        ret = self.__data[1]
        self.__swap(1, self.__count)
        self.__data.pop(self.__count)
        self.__count -= 1
        self.__shiftDown(1)
        return ret


def heapSort1(arr, n):
    maxHeap = MaxHeap()
    for i in range(n):
        maxHeap.insert(arr[i])
    for i in range(n):
        index = n - 1 - i
        arr[index] = maxHeap.extractMax()


def heapSort2(arr, n):
    maxHeap = MaxHeap()
    maxHeap.buildHeap(arr)
    for i in range(n):
        index = n - 1 - i
        arr[index] = maxHeap.extractMax()


def __shiftDown2(arr, n, k):
    temp = arr[k]
    # 判断有无孩子
    while (2 * k + 1 <= n - 1):
        j = 2 * k + 1
        if j + 1 < n and arr[j + 1] > arr[j]:
            j += 1
        if temp >= arr[j]:
            break
        arr[k] = arr[j]
        k = j
    arr[k] = temp


# 原地堆排序
def heapSort(arr, n):
    # 从最后一个非叶子节点开始 n-1-1 // 2
    for i in range((n - 1 - 1) // 2, -1, -1):
        __shiftDown2(arr, n, i)
    for i in range(n - 1, 0, -1):
        swap(arr, i, 0)
        __shiftDown2(arr, i, 0)


if __name__ == '__main__':
    # # 测试堆的数据结构
    # maxHeap = MaxHeap()
    # print(maxHeap.size())
    # for i in range(50):
    #     a = random.randint(0, 100)
    #     maxHeap.insert(a)
    #     # print(a)
    #
    # while(maxHeap.size() != 0):
    #     num = maxHeap.extractMax()
    #     print(num)

    n = 100000
    start = 0
    end = 100000
    # arr = genNearlyOrderArray(n, swapTimes=100)
    arr = genRandomArray(n, start, end)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    aTestSort(heapSort1, arr, n)
    aTestSort(heapSort2, arr2, n)
    aTestSort(sorting_advanced.quickSort2, arr3, n)
    aTestSort(sorting_advanced.quickSort3Ways, arr4, n)
    aTestSort(heapSort, arr5, n)
