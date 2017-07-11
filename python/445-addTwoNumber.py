# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        while l1:
            num1 *= 10
            num1 += l1.val
            l1 = l1.next
        num2 = 0
        while l2:
            num2 *= 10
            num2 += l2.val
            l2 = l2.next
        num = num1 + num2
        head = ListNode(num % 10)
        num /= 10
        while num:
            temp = ListNode(num % 10)
            num /= 10
            temp.next, head = head, temp
        return head
