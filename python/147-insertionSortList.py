class Solution(object):
    def insertionSortList(self, head):
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            if cur.val < cur.next.val:
                cur = cur.next ; continue
            if p.next.val > cur.next.val:
                p = dummy
            while p.next.val < cur.next.val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next

