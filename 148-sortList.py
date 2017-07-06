# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        if not (head and head.next):
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        sec = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(sec)
        head = root = ListNode(0)
        while l and r:
            if l.val < r.val:
                root.next = l
                l, root = l.next, root.next
            else:
                root.next = r
                r, root = r.next, root.next
        left = l or r
        while left:
            root.next = left
            left, root = left.next, root.next
        return head.next
