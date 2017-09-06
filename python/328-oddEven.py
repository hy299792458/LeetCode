class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head:
            return head
        
        odd = head
        even = head.next
        while even and even.next:
            temp = even.next
            even.next = even.next.next
            temp.next = odd.next
            odd.next = temp
            odd = odd.next
            even = even.next
            
        return head
