# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        res = ListNode(0)
        res.next = head
        
        def reverse(ent):
            p = ent.next
            l = []
            for _ in range(2):
                l.append(p)
                p = p.next
            for i in range(1, 2):
                l[- i].next = l[- i - 1]
            ent.next = l[-1]
            l[0].next = p
            return l[0]
        
        tail = res
        while True:
            try:
                tail = reverse(tail)
            except:
                return res.next
