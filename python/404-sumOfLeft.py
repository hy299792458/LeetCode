# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        self.re = 0
        def find(root, pos):
            if root.left:
                find(root.left, 0)
            if root.right:
                find(root.right, 1)
            if not (root.left or root.right):
                if pos == 0:
                    self.re += root.val
        if root:
            find(root, 1)
        return self.re
