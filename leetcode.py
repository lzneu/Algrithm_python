# -*- coding:utf-8 -*-

class StringFormat:
    def formatString(self, A, n, arg, m):
        # write code here
        A_list = A.split('%s')
        # 边界 若第一个元素是‘s%’
        if A[:1] == '%s':
            res = arg[0]
            arg.pop(0)
        else:
            res = ''
        for i in range(len(A_list)):
            res += A_list[i]
            if len(arg) != 0:
                res += arg[0]
                arg.pop(0)
        for c in arg:
            res += c
        return res

print(StringFormat().formatString('A%sC%sE', 7, ['B','D','F'], 3))