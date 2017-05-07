#!/usr/bin/env python
# coding=utf-8
import pdb

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Codec:
    ret = ''
    preR = []
    midR = []
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        def preorder(node):
            if not node: return
            self.preR.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
            return
        preorder(root)
        def midorder(node):
            if not node: return
            midorder(node.left)
            self.midR.append(str(node.val))
            midorder(node.right)
        midorder(root)
        self.ret=','.join(self.preR) + '\n' + ','.join(self.midR)
        return self.ret
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        preStr, midStr = data.split('\n')
        preList = [int(x) for x in preStr.split(',')]
        midList = [int(x) for x in midStr.split(',')]
        
        def reconstructTree(st,ed,k):
            pdb.set_trace()
            if st==ed: 
                node = TreeNode(midList[st])
                return node
            pos = -1
            for i in xrange(st,ed+1):
                if midList[i] == preList[k]:
                    pos = i
                    break
            node = TreeNode(preList[k])
            node.left = reconstructTree(st,pos-1,k+1)
            node.right = reconstructTree(pos+1,ed,k+pos-st)
            return node

        root = reconstructTree(0,len(preList)-1,0)
        return root



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    c = Codec()
    root = TreeNode(0)
    c.deserialize(c.serialize(root))
