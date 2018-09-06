#!/usr/bin/env python  
# coding=utf-8
import operator
def dec(l, r, hash_count):
    for i in range(l , r+1):
        hash_count[i] -= 1


res = 0
line = '8K67A65K27T59K346AK2'
# line = input()
# raw_input()里面不要有任何提示信息
hash_map = {'A': 1, '2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9,'T': 10,'J': 11,'Q': 12,'K': 13}
hash_count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}
tmp_list = []
for key in line:
    hash_count[hash_map[key]] += 1
    tmp_list.append(hash_map[key])
tmp_list.sort()
# 先出顺子
start = tmp_list[0]  # 从最小的开始
for i in range(tmp_list[0], tmp_list[-1]):
    if hash_count[i] >= 1:
        # 说明有值
        continue
    else:
        # 判断index是否大于4
        if i - start + 1 >= 5:
            # 可以减去这几个
            dec(start, i, hash_count)
            # 下一次从
            start = i+1
            res += 1


# 统计 四个和三个
list1 = 0
list2 = 0
list3 = 0
list4 = 0
for i in range(tmp_list[0], tmp_list[-1]):
    if hash_count[i] == 1:
        list1 +=1
    if hash_count[i] == 2:
        list2+=1
    if hash_count[i] == 3:
        list3+=1
    if hash_count[i] == 4:
        list4+=1
# 4个
res += list4
if list1 - list4*2 > 0:
    # 说明 剩下了单排
    pass
else:
    # 没有单排
    a = list1 - list4*2
    if a - list2*2 > 0:
        # 说明剩了几个
        pass
    else:
        pass