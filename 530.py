#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l=[]
        self.getAllNums(root,l)
        l.sort()
        Min = 2140000
        for i in range(1,len(l)):
            Min = min(Min,l[i]-l[i-1])
        
        return Min
        
    def getAllNums(self, root, l):
        if root == None:
            return
        l.append(root.val)
        self.getAllNums(root.left,l)
        self.getAllNums(root.right,l)
        return

