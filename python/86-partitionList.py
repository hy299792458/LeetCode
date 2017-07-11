# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        thr = x
        h1 = t1 = ListNode(0)
        h2 = t2 = ListNode(0)
        while head:
            if head.val < thr:
                t1.next = head
                t1 = head
            else:
                t2.next = head
                t2 = head
            head = head.next
        t1.next = h2.next
        t2.next = None
        return h1.next
