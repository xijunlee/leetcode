#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# trivial solution
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = []
        def dfs(node):
            if not node: return
            dfs(node.left)
            l.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return l[k-1]
            


