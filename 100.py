#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        plist = []
        qlist = []
        self.traverseTree(p,plist)
        self.traverseTree(q,qlist)
        if plist == qlist:
            return True
        else:
            return False
    
    def traverseTree(self, node, l):
        if node == None:
            l.append(-1)
            return
        l.append(node.val)
        self.traverseTree(node.left,l)
        self.traverseTree(node.right,l)
        return