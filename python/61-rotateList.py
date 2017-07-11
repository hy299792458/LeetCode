# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        if not head:
            return head
        l = 1
        tail = head
        while tail.next:
            l += 1
            tail = tail.next
        k = l - (k + 1) % l
        tail.next = head
        for _ in range(k):
            head = head.next
        newHead = head.next
        head.next = None
        return newHead
