# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        re = head
        while head:
            if head.next == None or head.next.val != head.val:
                head = head.next
            else:
                head.next = head.next.next
        return re
