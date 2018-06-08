# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 思路 返回值为 元素为字符串的list 递归过程为list中每个元素前面加上“root.val->”合并左右子树的list
        # 终止条件
        if root is None:
            return []
        # root为叶子结点时
        if not root.left and not root.right:
            return [str(root.val)]
        else:  # root 为非叶子结点
            path1 = self.binaryTreePaths(root.left)
            path2 = self.binaryTreePaths(root.right)
            res = []
            for str in path1 +path2:
                str1 = str(root.val)+'->'+str
                res.append(str1)
            return res
