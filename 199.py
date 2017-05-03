#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        queue = [(root,0)]
        head, tail = 0, 1
        while head < tail:
            cur, curDepth = queue[head]
            if cur:
                if cur.left: 
                    queue.append((cur.left,curDepth+1))
                    tail += 1
                if cur.right:
                    queue.append((cur.right,curDepth+1))
                    tail += 1
            head += 1
        node, minD = queue[-1]
        ans = []
        if node: ans.append(node.val)
        for i in xrange(len(queue)-1,-1,-1):
            node, d = queue[i]
            if d < minD:
                minD = d
                ans.append(node.val)
        return ans[::-1]

                
