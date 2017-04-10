#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
python可以在函数里面写函数！！！然后可以直接调用
'''

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        def helper(node):
            if not node:
                return
            ret.append(node.val)
            helper(node.left)
            helper(node.right)
            return
        helper(root)
        return ret
        

