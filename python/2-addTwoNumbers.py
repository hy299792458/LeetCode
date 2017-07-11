class Solution(object):
    def addTwoNumbers(self, l1, l2):
        tail, re = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            value = carry
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            tail.next = ListNode(value % 10)
            carry = value / 10
            tail = tail.next
        return re.next
