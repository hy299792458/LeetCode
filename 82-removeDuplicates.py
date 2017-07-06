# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        l = []
        while head:
            if not l or l[-1].val != head.val:
                l.append(head)
                head = head.next
            else:
                while head and head.val == l[-1].val:
                    head = head.next
                l.pop()
        if not l:
            return None
        else:
            for i in range(len(l) - 1):
                l[i].next = l[i + 1]
            l[-1].next = None
        return l[0]
