# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        m, n = min(m, n), max(m, n)
        res = ListNode(0)
        res.next = head
        tail = res
        for _ in range(m - 1):
            tail = tail.next
        ent = tail
        l = []
        for _ in range(n - m + 1):
            tail = tail.next
            l.append(tail)
        ext = l[-1].next
        for i in range(1, n - m + 1):
            l[- i].next = l[- i - 1]
        l[0].next = ext
        ent.next = l[-1]
        return res.next
