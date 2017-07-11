# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        self.re = 0
        def find(root, temp):
            value = temp * 10 + root.val
            if root.left:
                find(root.left, value)
            if root.right:
                find(root.right, value)
            if not root.left and not root.right:
                self.re += value
        if root:
            find(root, 0)
        return self.re
