#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ans = 0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def calcSubSum(node):
            if not node:
                return 0
            return node.val+calcSubSum(node.left)+calcSubSum(node.right)

        def calcTilt(node):
            if not node:
                return
            self.ans += abs(calcSubSum(node.left)-calcSubSum(node.right))
            calcTilt(node.left)
            calcTilt(node.right)
            return

        calcTilt(root)

        return self.ans


