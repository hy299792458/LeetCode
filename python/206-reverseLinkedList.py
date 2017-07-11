# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        pre = None
        temp = head
        while temp:
            nex = temp.next
            temp.next = pre
            pre = temp
            if nex:
                temp = nex
            else:
                return temp
