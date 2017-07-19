#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1, f = 0, 1
        while not l1:
            num1 += f*l1.val
            l1 = l1.next
            f *= 10
        num2, f = 0, 1
        while not l2:
            num2 += f*l2.val
            l2 = l2.next
            f *= 10
        num3 = num1+num2
        head = ListNode(num3%10)
        num3 /= 10
        p = head
        while num3:
            q = ListNode(num3%10)
            num3 /= 10
            p.next = q
            p = q
        return head


