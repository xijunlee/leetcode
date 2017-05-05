#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, pick, step):
            if not node: return 0
            if pick:
                return node.val+dfs(node.left,False)+dfs(node.right,False)
            if not pick:
                left1, left0 = dfs(node.left,True), dfs(node.left,False)
                righ1, right0 = dfs(node.right,True), dfs(node.right,False)
                return max(left0,left1) + max(right0,right1)

        return max(dfs(root,True),dfs(root,False))

