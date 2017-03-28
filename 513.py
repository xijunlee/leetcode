#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    ret = -1
    maxStep = -1
    
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root,0)
        return self.ret
        
    def dfs(self, node, step):
        if not node:
            return
    
        if step > self.maxStep:
            self.maxStep = step
            self.ret = node.val

        self.dfs(node.left,step+1)
        self.dfs(node.right,step+1)