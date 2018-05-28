#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : weighted_graph.py
# @Author: 投笔从容
# @Date  : 2018/5/28
# @Desc  : 带权图

'''
|-带权图:用python内置数据类型dict存储带权图的边
|-最小生成树问题和切分定理
    最小生成树：对于一个完全连通的具有v个结点的无向带权图，找到v-1条边使v个节点连通 且他们的权值之和最小
    切分定理：给定任意切分 横切边中权值最小的边必然属于最小生成树
        反证法可证
    prim算法的第一个实现：Lazy Prim
        时间复杂度O(ElogE)
    Prim算法优化
        利用索引堆
        时间复杂度O(ElogV)
        对于边的判断次数减少



'''
# 最小堆
class MinHeap:

    def __init__(self):
        self.__data = [0]
        self.__count = 0

    # 构造函数 给定一个数组创建一个最小堆 时间复杂度O(n)
    def buildHeap(self, arr):
        n = len(arr)
        self.__count = n
        self.__data = [0]
        self.__data.extend(arr)
        # 从非叶子结点开始😁逐个下移
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
        while (k > 1) and (self.__data[(k // 2)].weight() > self.__data[k].weight()):
            self.__swap(k // 2, k)
            k = k // 2

    def insert(self, item):
        self.__data.append(item)
        self.__count += 1
        self.__shiftUp(self.__count)

    def __shiftDown(self, k):
        # 判断有无左孩子
        while (2 * k <= self.__count):
            j = 2 * k  # 在此轮循环中 data[k] 与 data[j] 交换位置
            if (j + 1 <= self.__count and self.__data[j + 1].weight() < self.__data[j].weight()):
                j += 1
            if (self.__data[k].weight() <= self.__data[j].weight()):
                break
            self.__swap(k, j)
            k = j

    # 从队中去除堆顶元素 即堆中所存储的最大元素
    def extractMin(self):
        assert self.__count > 0

        ret = self.__data[1]
        self.__swap(1, self.__count)
        self.__data.pop(self.__count)
        self.__count -= 1
        self.__shiftDown(1)
        return ret


# 定义一个边的类
class Edge:
    def __init__(self, a, b, weight):
        self.__a = a
        self.__b = b
        self.__weight = weight

    def v(self):
        return self.__a

    def w(self):
        return self.__b

    def weight(self):
        return self.__weight

    def toString(self):
        return str(self.__a) + '-' + str(self.__b) + ':' + str(self.__weight)

    # 边之间的比较
    def compareTo(self, edge):
        if self.__weight > edge.weight():
            return +1
        elif self.__weight < edge.weight():
            return -1
        else:
            return 0

    def other(self, x):
        assert x == self.__a or x == self.__b
        if x == self.__a:
            return self.__b
        else:
            return self.__a


# 邻接矩阵实现稠密图
class DenseGraph:
    def __init__(self, n, directed):
        self.__m = 0  # 边数
        self.__n = n  # 顶点个数
        self.__directed = directed  # 是否有向图
        self.g = []
        temp_list = []
        for i in range(n):
            temp_list.append(None)
        for i in range(n):
            self.g.append(temp_list.copy())

    def V(self):
        return self.__n

    def E(self):
        return self.__m

    def addEdge(self, edge):
        assert 0 <= edge.v() < self.__n
        assert 0 <= edge.w() < self.__n

        # 若已经存在边
        if self.hasEdge(edge.v(), edge.w()):
            return
        # 这个地方有bug啊 排了好久都没看出那有问题 😔
        self.g[edge.v()][edge.w()] = Edge(edge.v(), edge.w(), edge.weight())
        if edge.v() != edge.w() and not self.__directed:
            self.g[edge.w()][edge.v()] = Edge(edge.w(), edge.v(), edge.weight())
        self.__m += 1

    def hasEdge(self, v, w):
        assert (v >= 0 and v < self.__n)
        assert (w >= 0 and w < self.__n)
        return self.g[v][w] is not None

    # 打印图的信息
    def show(self):
        for i in range(self.__n):
            print('vertex%d'% i, end=':\t')
            for j in range(self.__n):
                if self.g[i][j] is None:
                    print('None', end='\t')
                else:
                    print(('%s') % (str(self.g[i][j].weight())), end='\t')
            print('')

    # 返回v节点的邻接节点
    def getAdj(self, v):
        retList= []
        adjList= self.g[v]
        for adj in adjList:
            if adj is not None:
                retList.append(adj)
        return retList


# 稀疏图
class SparseGraph:
    def __init__(self, n, directed):
        self.__n = n
        self.__m = 0
        self.__directed = directed
        self.g = []
        for i in range(n):
            self.g.append([])

    def V(self):
        return self.__n

    def E(self):
        return self.__m

    def addEdge(self, edge):
        assert (0 <= edge.v() < self.__n)
        assert (0 <= edge.w() < self.__n)

        # 注意, 由于在邻接表的情况, 查找是否有重边需要遍历整个链表
        # 我们的程序允许重边的出现
        self.g[edge.v()].append(Edge(edge.v(), edge.w(), edge.weight()))
        if (edge.v() != edge.w() and not self.__directed):
            self.g[edge.w()].append(Edge(edge.v(), edge.w(), edge.weight()))
        self.__m += 1

    def hasEdge(self, v, w):
        assert (0 <= v < self.__n)
        assert (0 <= w < self.__n)

        for edge in range(self.g[v]):
            if edge.other(v) == w:
                return True
        return False

    # 打印邻接表
    def show(self):
        for v in range(self.__n):
            print('vertex%d' % v, end=':\t')
            for edge in self.g[v][: -1]:
                print(('to:%d,wt: %s') % (edge.w(), str(edge.weight())), end='\t')
            print(('to:%d,wt: %s') % (self.g[v][-1].w(), str(self.g[v][-1].weight())))

    # 返回v节点的邻接节点
    def getAdj(self, v):
        return self.g[v]


# 读取文件生成图数据结构的类
class ReadgRraph:
    # 从文件filename中读取图的信息, 存储进图graph中
    def __init__(self, graph, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
        f.close()
        assert len(lines) >= 1, '文件格式错误'
        self.V = int(lines[0].split(' ')[0])
        self.E = int(lines[0].split(' ')[1])
        edges = []
        for line in lines[1:]:
            edges.append(line.split(' '))
        assert self.V == graph.V(), '文件和图的顶点个数不一致'

        # 读取每一条边的信息
        for edge in edges:
            a = int(edge[0])
            b = int(edge[1])
            weight = float(edge[2])

            assert 0 <= a < self.V
            assert 0 <= b < self.V
            graph.addEdge(Edge(a, b, weight))


# 使用prim算法求解图的最小生成树
class LasyPrimMST:
    # 构造函数 使用Prim算法求图的最小生成树
    def __init__(self, graph):
        self.__G = graph  # 图的引用
        self.__pq = MinHeap()  # 最小堆 算法辅助的数据结构
        self.__marked = []  # 标记数组 在算法运行过程中边结点i是否被访问
        for i in range(graph.V()):
            self.__marked.append(False)
        self.__mst = []  # 最小生成树所包含的所有边

        # Lasy Prim
        self.__visit(0)
        while not self.__pq.isEmpty():
            # 使用最小堆找出已经访问的边中权值最小的边
            edge = self.__pq.extractMin()
            # 如果这条边的两端都已经访问过了 则扔掉这条边
            if (self.__marked[edge.v()] == self.__marked[edge.w()]):
                continue
            # 否则 这条边则应该存在在最小生成树中
            self.__mst.append(edge)
            # 访问和这条边链接的还没有访问过的结点
            if not self.__marked[edge.v()]:
                self.__visit(edge.v())
            else:
                self.__visit(edge.w())
        # 计算最小生成树的权值
        self.__mstWeight = self.__mst[0].weight()
        for i in range(1, len(self.__mst)):
            self.__mstWeight += self.__mst[i].weight()

    # 访问结点
    def __visit(self, v):
        assert not self.__marked[v]
        self.__marked[v] = True
        # 将和结点v相连接的所有为访问的边放入最小堆中
        edges = self.__G.getAdj(v)
        for edge in edges:
            if not self.__marked[edge.other(v)]:
                self.__pq.insert(edge)

    # 返回最小生成树的权值
    def result(self):
        return self.__mstWeight

    # 返回最小生成树的所有边
    def mstEdges(self):
        return self.__mst






if __name__ == '__main__':
    filename = './data/testG3.txt'
    g1 = SparseGraph(8, False)
    readGraph1 = ReadgRraph(g1, filename)
    g1.show()
    lasyPromMST1 = LasyPrimMST(g1)
    mst = lasyPromMST1.mstEdges()
    for i in range(len(mst)):
        print(mst[i].toString())
    print(lasyPromMST1.result())
    # g2 = DenseGraph(8, False)
    # readGraph2 = ReadgRraph(g2, filename)
    # g2.show()