#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    maxStep = -1
    ret = []
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.dfs(root,0)
        return self.ret
        
    def dfs(self, node, step):
        if not node:
            return
        if step > self.maxStep:
            self.ret.append(node.val)
            self.maxStep = step
        else:
            self.ret[step] = max(self.ret[step],node.val)
        self.dfs(node.left,step+1)
        self.dfs(node.right,step+1)
        