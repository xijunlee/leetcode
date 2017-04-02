#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    ret = []
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root)
        return self.ret
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.ret.append(node.val)
        self.dfs(node.right)
        return 
        

if __name__ == '__main__':
	s = Solution()
	print s.inorderTraversal([1,null,2,3])

