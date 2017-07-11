# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge(self, lists):
        if len(lists) == 2:
            a, b = lists
        else:
            return lists[0]
        res = ListNode(0)
        head = res
        while a and b:
            if a.val < b.val:
                res.next = a
                a, res = a.next, a
            else:
                res.next = b
                b, res = b.next, b
        while a:
            res.next = a
            a, res = a.next, a
        while b:
            res.next = b
            b, res = b.next, b
        return head.next
    def mergeKLists(self, lists):
        if not lists:
            return 
        while len(lists) > 1:
            temp = []
            p = 0
            while p < len(lists):
                temp.append(self.merge(lists[p:p+2]))
                p += 2
            lists = temp
        return lists[0]
