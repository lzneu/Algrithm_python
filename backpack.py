#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : backpack.py
# @Author: 投笔从容
# @Date  : 2018/6/13
# @Desc  : 背包问题与动态规划
'''
    问题描述：有一个背包，他的容量为C。现在有n种不同的物品 编号为0...n-1，其中每一件物品的重量为w(i)，价值为v(i)。问可以向这个背包中存放哪些物品，使得在不超过背包容量的基础上，物品的总价值最大

    解决思路：

    1. 暴力解法：每个物品都可以放进或者不放进背包，2^n种情况。n次运算选择最大的。

                        时间复杂度O((2^n)*n)

    2. 动态规划：状态F(n, C) 为将n个物品放进容量C的背包的最优解。参数为n和C两个。

                        i 状态 有两种选择： 放进第i个物品 和 不放 第i个物品

                        状态转移方程为: F(i, C) = max{ v(i)+F(i-1, C-w(i)) , F(i-1, C) }
    优化： 时间复杂度O(C*n)  空间复杂度O(C*n)
          空间复杂度可优化至O(2*C) = O(C): 只申请一个两行(一行也可以)的矩阵，反复利用
'''


class Solution:
    def backPack(self, w, v, C):
        '''

        :param w: list
        :param v: list
        :param C: int 背包最大容量
        :return: int
        '''
        n = len(w)
        if n == 0 or C == 0:
            return 0
        row = [-1 for i in range(C+1)]
        memo = [row.copy() for i in range(n)]
        # 第一行计算
        for i in range(C+1):
            if i >= w[0]:
                memo[0][i] = v[0]
            else:
                memo[0][i] = 0

        for i in range(1, n):  # 增加i个物品后的最优化计算
            for j in range(C+1):  # 第i个物品 第j个位置的最大价值
                if j >= w[i]:
                    memo[i][j] = max(v[i]+memo[i-1][j-w[i]], memo[i-1][j])
                else:  # j < w[i]
                    memo[i][j] = memo[i-1][j]
        return memo[n-1][C]

# 测试
w = [1,2,3]
v = [6,10,12]
C = 5
print(Solution().backPack(w, v,C))