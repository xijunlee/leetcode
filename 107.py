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
    
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dfs(root)
        if root:
            self.ret.append([root.val])
        return self.ret
    
    def dfs(self, node):
        if not node:
            return
        l = []
        if node.left:
            l.append(node.left.val)
        if node.right:
            l.append(node.right.val)
        self.dfs(node.left)
        self.dfs(node.right)
        if len(l):
            self.ret.append(l)
        return
        
        