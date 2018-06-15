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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # 返回值为 (偷该房间获得的最大money, 不偷该房间获得的最大money)
    def __dfs(self, root):
        money1, money2 = 0, 0
        if root is None:
            return money1, money2

        # 深度优先遍历
        res1 = self.__dfs(root.left)
        res2 = self.__dfs(root.right)
        money1 = root.val + res1[1] + res2[1]
        money2 = max(res1[0], res1[1]) + max(res2[0], res2[1])
        print('结点%d:  选%d++不选%d' % (root.val, money1, money2))
        return money1, money2

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 思路 两次深度优先遍历？
        res = self.__dfs(root)
        return max(res[1], res[0])


root = createTree([4,1,None,2,None,3])
res = Solution().rob(root)
print(res)
