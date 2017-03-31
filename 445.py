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
        num1, num2 = 0, 0 
        a1, a2, a3= [], [], []
        while l1:
            a1.append(l1.val)
            l1 = l1.next
        while l2:
            a2.append(l2.val)
            l2 = l2.next

        p = 1
        while a1:
            num1 += a1.pop()*p
            p *= 10
        p = 1
        while a2:
            num2 += a2.pop()*p
            p *= 10
        num3 = num1 + num2
        while num3 > 0:
            a3.append(num3%10)
            num3 /= 10
        p = ListNode(a3.pop())
        tmp = p
        while a3:
            l = ListNode(a3.pop())
            tmp.next = l
            tmp = tmp.next
        return p
      
            
            