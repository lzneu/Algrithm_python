#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : AntiOrder.py
# @Author: 投笔从容
# @Date  : 2018/5/23
# @Desc  : 求一个数组的逆序对

# -*- coding:utf-8 -*-

class AntiOrder:
    def __mergeSort(self, arr, l, r):
        count = 0
        if l >= r:
            return count
        mid = int((l + r) / 2)
        count1 = self.__mergeSort(arr, l, mid)
        count2 = self.__mergeSort(arr, mid + 1, r)
        if (arr[mid] > arr[mid + 1]):
            count = self.__merge(arr, l, mid, r)
        count = count + count1 + count2
        return count

    def __merge(self, arr, l, mid, r):
        count = 0
        aux = arr[l: r + 1]
        i = l
        j = mid + 1
        for k in range(l, r + 1):
            if (i > mid):
                arr[k] = aux[j-l]
                j += 1
            elif (j > r):
                arr[k] = aux[i-l]
                i += 1
            elif (aux[i - l] < aux[j - l]):
                arr[k] = aux[i - l]
                i += 1
                # count += r + 1 - j
            else:
                arr[k] = aux[j - l]
                j += 1
                count += mid + 1 - i
        return count

    def count(self, A, n):
        # write code here
        # 利用归并排序计算逆序对数
        return self.__mergeSort(A, 0, n-1)
a = AntiOrder()
print(a.count([1,2,3,4,5,6,7,0], 8))