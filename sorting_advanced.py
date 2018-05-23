#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : sorting_advanced.py
# @Author: 投笔从容
# @Date  : 2018/5/21
# @Desc  : 高级排序

'''
源代码:

O(n*logn)级别的排序:
|-归并排序
    分成log(n)个层级 每个层级进行O(n)排序
    每次归并时 开辟一个新的存储空间作为辅助 因此需要使用O(n)多的空间
    用三个索引进行归并 时间复杂度O(n)
    当n比较小的时候 由于复杂度前面都有常数项 因此 归并有时比插入排序满 可在此处进行优化
    自底向上的归并排序 由于没有用到数组下标 因此可以用于链表排序O(n*logn)
|-快速排序
    选定元素挪到正确位置,挪动的过程也是分离大于选定元素 和 小于选定元素的过程
    递归选定元素两侧的数组进行快排
    当集合完全有序时 快拍退化成了O（n^2）级别 这是可以通过随机选取每次快排的枢轴来优化
|-二路快排
    当集合中的元素大量重复时 相等于temp的元素很多 导致数据集合分成了两个不平衡的部分 ,改进patition函数的切分方式,变成双路快排

|-三路快排
    分割时将集合分成三部分
        =temp
        <temp
        >temp
        递归的分割后两个部分

总结: 归并排序 和 快速排序 都使用了分治算法
扩展应用:
    实现方法见我的github:
    |- 求逆序对
        完全有序的数列 逆序对数量为0 逆序的数列 逆序对数量最多
        可以通过求逆序对的数量来表示数列的有序程度
        暴力解法O(n^2)
        归并排序求逆序对 O(n*logn) swap一次 说明有一个逆序对 可以叠加

    |- 求数组的第N大元素
        利用快速排序 patition只留下 符合要求的那部分 知道 temp就是第n个
        复杂度O(n)
'''

# 生成一个近乎有序的数组
import datetime
import random
import numpy as np

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


# 将arr[l...mid] 和 arr[mid+1...r]两部分合并
def __merge(arr, l, mid, r):
    aux = arr[l: r + 1]
    i = l
    j = mid + 1
    for k in range(l, r + 1):

        if (i > mid):
            arr[k] = aux[j - l]
            j += 1
        elif (j > r):
            arr[k] = aux[i - l]
            i += 1
        elif (aux[i - l] < aux[j - l]):
            arr[k] = aux[i - l]
            i += 1
        else:
            arr[k] = aux[j - l]
            j += 1


def insertionSort4Ms(arr, l, r):
    # if l >= r:
    #     return
    for i in range(l + 1, r + 1):
        j = i
        temp = arr[i]
        while ((j > l) and (arr[j - 1] > temp)):
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = temp
    return


# 递归的使用归并排序arr[l...r]
def __mergeSort(arr, l, r):
    # if l >= r:
    #     return
    # 此处优化 在n比较小时 调用插入排序
    if (r - l) <= 15:
        insertionSort4Ms(arr, l, r)
        return
    mid = int((l + r) / 2)
    __mergeSort(arr, l, mid)
    __mergeSort(arr, mid + 1, r)
    # 若有序 无需再合并了
    if (arr[mid] > arr[mid + 1]):
        __merge(arr, l, mid, r)


def mergeSort(arr, n):
    # 表示私有
    __mergeSort(arr, 0, n - 1)


# 自底向上归并排序(由于没有用到数组下标 因此可以用于链表排序)
def mergeSortBU(arr, n):
    size = 1
    while (size <= n):
        i = 0
        while (i + size < n):
            __merge(arr, i, i + size - 1, min(i + size + size - 1, n - 1))
            i += (size + size)
        size += size


# 对arr[l...r]进行partition
def __partition(arr, l, r):
    # 此处对快排进行优化，随机中选取元素作为枢轴
    swap(arr, l, random.randint(l, r))
    temp = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if (temp > arr[i]):
            swap(arr, j + 1, i)
            j += 1
    swap(arr, j, l)
    return j


# 对arr[l...r]进行快速排序
def __quickSort(arr, l, r):
    # if (l>=r):
    #     return  # 别忘了这个啊 要不然死循环了
    if (r - l) <= 15:
        # 元素个数少的时候用插入排序
        insertionSort4Ms(arr, l, r)
        return
    p = __partition(arr, l, r)
    __quickSort(arr, l, p - 1)
    __quickSort(arr, p + 1, r)


# 快速排序
def quickSort(arr, n):
    __quickSort(arr, 0, n - 1)


def __partition2(arr, l, r):
    swap(arr, l, random.randint(l, r))
    temp = arr[l]
    i = l + 1
    j = r
    while True:
        while (i <= r and arr[i] < temp):
            i += 1
        while (j >= l + 1 and arr[j] > temp):
            j -= 1
        if (j < i):
            break
        swap(arr, j, i)
        i += 1
        j -= 1
    # temp所在的位置是<=temp的一段 因此需要将其与j交换
    swap(arr, l, j)
    return j


def __quickSort2(arr, l, r):
    if (r - l) <= 15:
        insertionSort4Ms(arr, l, r)
        return
    p = __partition2(arr, l, r)
    __quickSort2(arr, l, p - 1)
    __quickSort2(arr, p + 1, r)


# 二路快排 将=temp的元素分散到两个集合中,避免平衡树不平衡
def quickSort2(arr, n):
    __quickSort2(arr, 0, n - 1)


def __partition3Ways(arr, l, r):
    swap(arr, l, random.randint(l, r))
    temp = arr[l]

    lt = l  # arr[l+1...lt] < temp
    gt = r + 1  # arr[gt...r] > temp
    i = l + 1  # arr[lt+1...i] == temp
    while (i < gt):
        # i==gt时表示已经比较结束
        if (arr[i] < temp):
            swap(arr, i, lt + 1)
            lt += 1
            i += 1
        elif (arr[i] > temp):
            swap(arr, i, gt - 1)
            gt -= 1

        else:  # arr[i] == temp
            i += 1
    swap(arr, l, lt)
    return lt, gt


def __quickSort3Ways(arr, l, r):
    if (r - l) <= 15:
        insertionSort4Ms(arr, l, r)
        return
    lt, gt = __partition3Ways(arr, l, r)
    __quickSort3Ways(arr, l, lt - 1)
    __quickSort3Ways(arr, gt, r)


def quickSort3Ways(arr, n):
    __quickSort3Ways(arr, 0, n-1)


if __name__ == '__main__':
    n = 100000
    start = 0
    end = 10000
    arr = genNearlyOrderArray(n, swapTimes=100)
    arr = genRandomArray(n, start, end)
    arr2 = arr[:]
    arr3 = arr[:]
    arr4 = arr[:]
    aTestSort(mergeSort, arr, n)
    # aTestSort(quickSort, arr2, n)
    aTestSort(quickSort2, arr3, n)
    aTestSort(quickSort3Ways, arr4, n)
