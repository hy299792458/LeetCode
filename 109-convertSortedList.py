# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        if not head:
            return None
        tail = None
        slow = head
        fast = head.next
        while fast and fast.next:
            tail, slow = slow, slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        sec = slow.next
        if tail:
            tail.next = None
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(sec)
        return root
