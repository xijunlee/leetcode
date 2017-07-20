#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        ans.sort()
        head = ListNode(ans[0])
        p = head
        for i in xrange(1,len(ans)):
            p.next = ListNode(ans[i])
            p = p.next
        return head
        