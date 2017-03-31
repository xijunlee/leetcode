#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import random

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head
        k = 0
        tmp = head
        while tmp:
            k += 1
            tmp = tmp.next
        self.length = k
        

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        r = int(random.random()*self.length*2)%self.length
        p = self.head
        k = 0
        while k<r:
            p = p.next
            k += 1
        
        return p


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()