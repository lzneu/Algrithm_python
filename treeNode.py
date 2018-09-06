# -*- coding:utf-8 -*-
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from queue import Queue
import collections
# 需要用队列
def createTree(lists):
    if len(lists) == 0:
        return None

    root = TreeNode(lists[0])
    # q = Queue()
    q = Queue()
    q.put(root)
    i = 1
    n = len(lists)
    while i < n:
        node = q.get()
        if lists[i] != None:
            node.left = TreeNode(lists[i])
            q.put(node.left)
        else:
            node.left = None
        i += 1
        if i < n:
            if lists[i] != None:
                node.right = TreeNode(lists[i])
                q.put(node.right)
            else:
                node.right = None
            i += 1
    return root


class Solution:
    def __init__(self):
        pass

    def preOrder(self, root):
        if root:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)

    # 先序遍历非递归形式 用栈来实现
    def preOrderNcur(self,root):
        stack = []
        while True:
            # 循环到最左节点处
            while root is not None:
                print(root.val)
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            root = stack.pop()
            root = root.right

    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            print(root.val)
            self.inOrder(root.right)

    # 中序遍历非递归形式
    def inOrderNcur(self, root):
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if len(stack) == 0:
                break
            root = stack.pop()
            print(root.val)
            root = root.right

    def postOrder(self,root):
        # 终止条件
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print(root.val)

    # 非递归过程的后序遍历 这个时候需要一个标记位标识该节点被访问过几次 只有两次才能打印
    def postOrderNcur(self, root):
        stack = []
        stack_flag = []
        while True:
            while root is not None:
                stack.append(root)
                stack_flag.append(False)
                root = root.left
            # 从左子树过来的 现在要 遍历右子树 或者 输出根节点值
            while len(stack) != 0 and stack_flag[-1] == True:
                # 可以输出根节点了
                root = stack.pop()
                stack_flag.pop()
                print(root.val)
            if len(stack) != 0:  # 否则是没有访问右子树 需要先访问右子树
                stack_flag.pop()
                stack_flag.append(True)
                root = stack[-1]
                root = root.right
            else:
                break


root = createTree([8,6,10,5,7,9,11])
Solution().postOrderNcur(root)