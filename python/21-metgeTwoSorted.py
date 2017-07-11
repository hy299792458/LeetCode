# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        re = ListNode(0)
        tail = re
        while l1 and l2:
            if l1.val < l2 .val:
                tail.next = l1
                tail, l1 = l1, l1.next
            else:
                tail.next = l2
                tail, l2 = l2, l2.next
        while l1:
            tail.next = l1
            tail, l1 = l1, l1.next
        while l2:
            tail.next = l2
            tail, l2 = l2, l2.next
        return re.next
