# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            p1 = head
            p2 = head.next
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next.next
            return True
        except:
            return False
