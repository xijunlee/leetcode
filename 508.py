#!/usr/bin/env python
# coding=utf-8

'''
学到了:
1、python中的collections模块中的Counter类，其本质就是一个用来计数的dict
2、列表元素的快速迭代写法[k for k in self.c.keys() if self.c[k] == most_freq]
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution(object):
    c = Counter()
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.helper(root)
        most_freq = max(self.c.values())
        return [k for k in self.c.keys() if self.c[k] == most_freq]
            
    
    def helper(self, node):
        if not node:
            return 0
        sum = node.val+self.helper(node.left)+self.helper(node.right)
        self.c[sum] += 1
        return sum
        
