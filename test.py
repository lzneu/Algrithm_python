class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:

    def maxPoints(self, points):
        from fractions import Fraction
        """
        :type points: List[Point]
        :rtype: int
        """
        # 思路
        '''
        第一层循环 取第i个点
            第二层取剩下的点 构建一个map key为两个点的k value为频数
            统计每个i对应的最大频数
            注意重复点 每个k都要多加 因此要统计重复i的个数
            注意斜率不存在时单独设一个k
            注意只有重复点的情况
        '''
        if len(points)<3:
            return len(points)
        res = 0
        for i in range(len(points)-1):
            # 构建哈希表
            hash_map = {}
            # 重复计数
            iCount = 1
            for j in range(i+1, len(points)):
                # 重复值统计
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    iCount += 1
                else:
                    if points[i].x == points[j].x:
                        k = 'max'
                    else:
                        k = 10.0 * (points[j].y - points[i].y) / (points[j].x - points[i].x)

                    if k in hash_map:
                        hash_map[k] += 1
                    else:
                        hash_map[k] = 1

            for v in hash_map.values():
                res = max(res, v+iCount)
            res = max(res, iCount)
        return res

# class Solution(object):
#     def maxPoints(self, points):
#         ret = 0
#         length = len(points)
#         for i in range(length):
#             slopeCnt = {}
#             same = 0
#             for j in range(i + 1, length):
#                 # same point
#                 if self.isEqual(points[i], points[j]):
#                     same += 1
#                 else:
#                     k = self.getK(points[i], points[j])
#                     if slopeCnt.get(k) is None:
#                         slopeCnt[k] = 1
#                     else:  # same slope
#                         slopeCnt[k] += 1
#             val = max(slopeCnt.values()) if len(slopeCnt) else 0
#             ret = max(ret, val + same + 1)
#         return ret

    # def getK(self, pa, pb):
    #     if pa.x == pb.x:
    #         return None
    #     return 10.0 * (pb.y - pa.y) / (pb.x - pa.x)
    #
    # def isEqual(self, pa, pb):
    #     return pa.x == pb.x and pa.y == pb.y

a = [[0,0],[94911151,94911150],[94911152,94911151]]
points = []
for i in a:
    points.append(Point(i[0], i[1]))

print(Solution().maxPoints(points))