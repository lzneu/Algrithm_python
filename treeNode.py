# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
from queue import Queue
# 需要用队列
def createTree(lists):
    if len(lists) == 0:
        return None

    root = TreeNode(lists[0])
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
    def __findPath(self, root, sum):
        if root is None:
            return 0
        res = 0
        if root.val ==sum:
            res += 1
        res += self.__findPath(root.left, sum - root.val)
        res += self.__findPath(root.right, sum - root.val)
        return res


    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # 递归过程包括两个部分 一个是包含root的路径寻找 另一个是不包含root的路径寻找
        if root is None:
            return 0
        # 包含root的路径
        res = self.__findPath(root, sum)
        # 不包含root
        res += self.pathSum(root.left, sum)
        res += self.pathSum(root.right, sum)
        return res


root = createTree([10,5,-3,3,2,None,11,3,-2,None,1])
print(Solution().pathSum(root, 8))