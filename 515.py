#!/usr/bin/env python
# coding=utf-8

'''
1、复习了用队列来做bfs的知识点
2、学到了python中any来巧妙处理队列中元素的存在与否
'''

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
        maxes = []
        row = [root]
        while any(row):
            maxes.append(max([n.val for n in row]))
            tmp = []
            for node in row:
                for kid in (node.left,node.right):
                    if kid: tmp.append(kid)
            row = tmp
        return maxes
            
            
        
        