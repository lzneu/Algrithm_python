#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : LCS.py
# @Author: 投笔从容
# @Date  : 2018/6/15
# @Desc  : 最长公共子序列

'''
问题：给定两个字符串S1和S2,求这两个字符串的最长公共子序列的长度
例子：
    S1= ABCD
    S2=AEBD
    最长公共子序列长度为3
思路：
    1.自顶向下的方法
        |-回溯法： 时间复杂度O(2^n * n)
            |-对两字符串的最后一个字符进行比较，分为相等和不相等两种情况
                |-相等：res = 1 + back(m-1, n-1)
                |-不相等：res = max(back(m, n-1), back(m-1, n))
                |-其中m，n分别为两个字符串的最后一个元素的索引，back为递归调用的寻找最长公共子序列的函数
        |-结构化子函数：时间复杂度O(m*n)
    2.自底向上的方法
        |-二维的动态规划：
            |-状态LCS(m, n)：表示S1[0...m-1]和S2[0...n-1]的最长公共子序列的长度
            |-m, n 为LCS中新增加的两个字符，我们只需要考虑当前新增这两个字符后的状态转移即可。
            |-状态转移方程分为两种情况：
                |-1. S1[m] == S2[n]: LCS(m, n)=1+LCS(m-1,n-1)
                |-2. S1[m] != S2[N]: LCS(m, n)=max(Lcs(m-1, n), LCS(m, n-1))
            |-时间复杂度O(m*n)
'''

class Solution(object):
    # 1 回溯法
    def back(self, S1, S2):
        m = len(S1)-1
        n = len(S2)-1
        # 终止条件
        if m < 0 or n < 0:
            return 0
        # 递归过程
        if S1[m] == S2[n]:
            return 1+self.back(S1[:m], S2[:n])
        else:
            # 不相等
            return max(self.back(S1[:m], S2), self.back(S1, S2[:n]))

    # 2 结构化子函数
    def childS(self, S1, S2):
        m = len(S1) - 1
        n = len(S2) - 1
        rows = [-1 for i in range(n + 1)]
        memo = [rows.copy() for j in range(m + 1)]
        return self.struct(S1, S2, memo)
    def struct(self, S1, S2, memo):
        m = len(S1) - 1
        n = len(S2) - 1
        # 终止条件
        if m < 0 or n < 0:
            return 0

        if S1[m] == S2[n]:
            if memo[m-1][n-1] == -1:
                memo[m - 1][n - 1] = self.struct(S1[:m], S2[:n], memo)+1
            return memo[m-1][n-1]
        else:
            if memo[m-1][n] == -1:
                memo[m - 1][n] = self.struct(S1[:m], S2, memo)
            if memo[m][n-1] == -1:
                memo[m][n - 1] = self.struct(S1, S2[:n], memo)
            return max(memo[m][n - 1], memo[m-1][n])

    # 3 动态规划
    def dp(self, S1, S2):
        m = len(S1)
        n = len(S2)
        if m < 0 or n < 0:
            return 0
        memo = [[0]*(n+1) for j in range(m+1)]
        # 初始状态 第0行 第0列 都是0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if S1[i-1] == S2[j-1]:  # S1中的第i个字符 S2中的第j个字符
                    memo[i][j] = 1 + memo[i-1][j-1]
                else:
                    memo[i][j] = max(memo[i-1][j], memo[i][j-1])
        return memo[m][n]

S1 = 'AFDSAFDSA'
S2 = 'FDSAFD'
print(Solution().dp(S1, S2))
