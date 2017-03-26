# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root.left)+self.dfs(root.right)+1
    
    def dfs(self, root):
        if not root:
            return 0
        return max(self.dfs(root.left),self.dfs(root.right))+1