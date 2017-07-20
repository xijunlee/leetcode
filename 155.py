#!/usr/bin/env python
# coding=utf-8

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        currentMin = self.getMin()
        if currentMin == None or currentMin > x:
            currentMin = x
        self.stack.append([x,currentMin])
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack)>0:
            return self.stack[-1][0]
        else: return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0: return None
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

