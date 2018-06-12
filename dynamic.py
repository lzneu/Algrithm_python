#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : dynamic.py
# @Author: 投笔从容
# @Date  : 2018/6/12
# @Desc  : 动态规划

'''
动态规划
    \-定义:将原问题拆解成若干子问题,同时保存子问题的答案,使得每个子问题只求解一次,最终获得原问题的答案
    \-解决的问题:
        递归问题->重叠子问题 -> 记忆化搜索(自顶向下的解决问题)
                         -> 动态规划(自底向上的解决问题)
'''


# 递归的的斐波那契数列解决方法 时间复杂度O(2^n)
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
# print(fib(50))

# 动态规划 先解决小数据量的 再层层递推的解决大数据量级的问题 时间复杂度O(n)
def fib2(n):
    memo = [-1 for x in range(n+1)]
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[n]
# print(fib2(50))

# 记忆化搜索
MAXSIZE = 1000
memo = [-1 for i in range(MAXSIZE)]
def fib3(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if memo[n] == -1:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]
print(fib3(40))
