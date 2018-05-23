#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Finder.py
# @Author: 投笔从容
# @Date  : 2018/5/23
# @Desc  : 寻找数组中的第K大元素

import random


class Finder:
    def swap(self, arr, i, j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp

    def __partition(self, arr, l, r):
        self.swap(arr, l, random.randint(l, r))
        temp = arr[l]
        i = l + 1
        j = r
        while True:
            while (i <= r and arr[i] < temp):
                i += 1
            while (j >= l + 1 and arr[j] > temp):
                j -= 1
            if (i > j):
                break
            self.swap(arr, i, j)
            i += 1
            j -= 1
        self.swap(arr, l, j)
        return j

    def __quickSort(self, arr, l, r, k):
        if (l >= r):
            return arr[l]
        p = self.__partition(arr, l, r)
        if p == k:
            return arr[p]
        elif (p > k):
            return self.__quickSort(arr, l, p - 1, k)
        else:
            return self.__quickSort(arr, p + 1, r, k)

    def findKth(self, a, n, K):
        # write code here
        return self.__quickSort(a, 0, n - 1, n - K)