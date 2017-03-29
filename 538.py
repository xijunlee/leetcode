# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    l = []
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        
        i = len(self.l)-2
        while i>= 0:
            self.l[i].val += self.l[i+1].val
            i -= 1
            
        return root
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.l.append(node)
        self.dfs(node.right)
        return

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    l = []
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        
        i = len(self.l)-2
        while i>= 0:
            self.l[i].val += self.l[i+1].val
            i -= 1
            
        return root
        
    def dfs(self, node):
        if not node:
            return
        self.dfs(node.left)
        self.l.append(node)
        self.dfs(node.right)
        return