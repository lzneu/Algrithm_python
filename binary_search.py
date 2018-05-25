#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : binary_search.py
# @Author: 投笔从容
# @Date  : 2018/5/25
# @Desc  : 二分查找
'''
|-二分查找法
    时间复杂度O(logn)
|-二分搜索树
    特点：
        高效 不接可以查找数据 插入删除数据的复杂度都是O(logn)
        可以方便的回答很多数据之间的关系
        min max floor ceil select
    定义：
        二叉树（不一定是完全二叉树）
        每个节点的键值大于左孩子、小于右孩子
        以左右孩子为根的子树仍为二分搜索树（递归结构）
|-二分搜索树的遍历
    深度优先：
        前序遍历：
        中序遍历：可以对二分搜索树进行排序
        后序遍历：可以用于节点的释放
    广度优先：
        层序遍历：用一个队列实现
|-删除一个节点
    寻找二分搜索树的最大值和最小值：
        一直往左找坐孩子，知道左孩子不存在 该节点为最小值 最大值同理
    删除最大值/最小值

    二分搜索树删除节点
        只有左孩子：左孩子上移
        只有右孩子：右孩子上移
        左右孩子都有节点：右孩子的最左节点上移
            即找到要删除的节点的后继节点 代替该节点
            时间复杂度O（logn）

|-二分搜索树的局限性
    同样的数据 可以对应不同的二分搜索树
    二分搜索树可能退化成链表 搜索复杂度O(n) 实际上比顺序搜索还要慢 因为存在左右孩子存储和递归的消耗
        解决方案：平衡二叉树
            红黑树实现平衡二叉树


'''

from queue import Queue


# 二分查找 有序数组arr 查找target
def binarySearch(arr, n, target):
    # 在arr[l...r]中查找target
    l = 0
    r = n - 1
    while (l <= r):
        # mid = (l+r) // 2 # 此处可能产生整型溢出
        mid = l + (r - l) // 2
        if (arr[mid] == target):
            return mid
        if (target < arr[mid]):
            r = mid - 1
        else:
            l = mid + 1
    # 没找到 返回-1
    return -1


# 二分搜索树
class BST:
    # 树中的节点为私有的类 外界不需要了解二分搜索树的具体实现
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.left = self.right = None

    def __init__(self):
        self.__root = None
        self.__count = 0

    def size(self):
        return self.__count

    def isEmpty(self):
        return self.__count == 0

    # 插入一个新的节点 采用递归结构, 返回插入新节点后的二叉搜索树的根
    def insert(self, key, value):
        self.__root = self.__insert(self.__root, key, value)

    # 以node为根的二分搜索树中是否包含键值为key的节点 使用递归算法
    def contain(self, key):
        return self.__contain(self.__root, key)

    # 以node为根结点的二分搜索树中查找key对应的value， 若value不存在 返回null
    def search(self, key):
        return self.__search(self.__root, key)

    # 二叉树的前序遍历
    def preOrder(self):
        self.__preOrder(self.__root)

    # 二叉树的中序遍历
    def inOrder(self):
        self.__inOrder(self.__root)

    # 二叉树的后序遍历
    def postOrder(self):
        self.__postOrder(self.__root)

    # 二分搜索树的层序遍历 利用队列的数据结构
    def levelOrder(self):
        # 初始化一个队列
        q = Queue()
        q.put(self.__root)
        while not q.empty():
            node = q.get()
            print(node.key)
            if node.left is not None:
                q.put(node.left)
            if node.right is not None:
                q.put(node.right)

    # 寻找二分搜索树的最小键值
    def minimum(self):
        if self.__count <= 0:
            print('二分搜索树里面没有元素了！！！')
            raise IndexError
        minNode = self.__minimum(self.__root)
        return minNode.key

    # 寻找树中的最大键值
    def maxmum(self):
        if self.__count <= 0:
            print('二分搜索树里面没有元素了！！！')
            raise IndexError
        maxNode  = self.__maxmum(self.__root)
        return maxNode.key

    # 从二分搜索属树种删除最小值所在节点
    def removeMin(self):
        if self.__root is not None:
            self.__root = self.__removeMin(self.__root)

    def removeMax(self):
        if self.__root is not None:
            self.__root = self.__removeMax(self.__root)

    # 从二分搜索树种删除键值为key的节点
    def remove(self, key):
        self.__root = self.__remove(self.__root, key)

    '''
    二分搜索树辅助函数
    '''
    # 删除以node为根的二分搜索树种键值为key的节点，递归算法
    # 返回删除后的节点后新的二分搜索树
    def __remove(self, node, key):
        if node is None:
            return None
        # 递归寻找
        if key > node.key:
            node.right = self.__remove(node.right, key)
            return node
        elif key < node.key:
            node.left = self.__remove(node.left, key)
            return node
        else:  # key==node.key的情况
            # 待删除的节点左子树为空
            if node.left is None:
                rightNode = node.right
                node.right = None
                self.__count -= 1
                return rightNode
            # 待删除的节点右子树为空
            if node.right is None:
                leftNode = node.left
                node.left = None
                self.__count -= 1
                return leftNode

            # 待删除的节点左右节点都不为空的情况
            # 找到比待删除节点大的最小节点 即待删除节点右子树的最小节点
            # 用这个节点顶替待删除节点的位置
            successor = self.Node(node.key, node.value)
            self.__count += 1
            successor.right = self.__removeMin(node.right)
            successor.left = node.left

            node.left = node.right = None
            self.__count -= 1

            return successor


    # 删除掉以node为根的二分搜索书中的最小节点
    # 返回删除节点后的二分搜索树的根节点
    def __removeMin(self, node):
        if node.left is not None:
            rightNode  = node.right
            print(node.key)
            print('已经删除')
            node.right = None
            self.__count -= 1
            return rightNode

        node.left = self.__removeMin(node.left)
        return node

    # 删除掉以node为根的二分搜索书中的最大节点
    # 返回删除节点后的二分搜索树的根节点
    def __removeMax(self, node):
        if node.right is not None:
            leftNode = node.left
            print(node.key)
            print('已经删除')
            node.left = None
            self.__count -= 1
            return leftNode
        node.right = self.__removeMax(node.right)
        return node

    def __minimum(self, node):
        if (node.left is None):
            return node
        return self.__minimum(node.left)

    def __maxmum(self, node):
        if node.right is None:
            return node
        return self.__maxmum(node.right)

    def __insert(self, node, key, value):
        if (node is None):
            self.__count += 1
            return self.Node(key, value)

        if (key == node.key):
            node.value = value
        elif (key > node.key):
            node.right = self.__insert(node.right, key, value)
        else:
            node.left = self.__insert(node.left, key, value)
        return node

    def __contain(self, node, key):

        if node is None:
            return False
        if (key == node.key):
            return True
        elif (key > node.key):
            return self.__contain(node.right, key)
        else:
            return self.__contain(node.left, key)

    def __search(self, node, key):
        if node is None:
            return None
        if key == node.key:
            return node.value
        elif key > node.key:
            return self.__search(node.right, key)
        else:
            return self.__search(node.left, key)

    def __preOrder(self, node):
        if node is not None:
            print(node.key)
            self.__preOrder(node.left)
            self.__preOrder(node.right)

    def __inOrder(self, node):
        if node is not None:
            self.__inOrder(node.left)
            print(node.key)
            self.__inOrder(node.right)

    def __postOrder(self, node):
        if node is not None:
            self.__postOrder(node.left)
            self.__postOrder(node.right)
            print(node.key)


from tools import *
if __name__ == '__main__':
    n = 100000
    start = 0
    end = 100000
    arr = genNearlyOrderArray(n, swapTimes=50000)
    # arr = genRandomArray(n, start, end)
    arr2 = arr.copy()
    arr3 = arr.copy()
    arr4 = arr.copy()
    arr5 = arr.copy()
    print(arr)
    bst = BST()
    # 测试的搜索二叉树的键类型为int 值类型为string
    for i in range(n):
        bst.insert(arr[i], str(arr[i]))
    maxN = bst.maxmum()
    print(maxN)
    bst.remove(99999)
    print(bst.maxmum())

