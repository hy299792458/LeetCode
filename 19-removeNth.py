# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        res = ListNode(0)
        res.next = head
        p1 = p2 = res
        for _ in range(n + 1):
            p2 = p2.next
        while p2:
            p2 = p2.next
            p1 = p1.next
        p1.next = p1.next.next
        return res.next
