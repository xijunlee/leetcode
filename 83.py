# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        while node:
            tmp = node
            while tmp and node.val == tmp.val:
                tmp = tmp.next
            node.next = tmp
            node = node.next
        return head
            
        