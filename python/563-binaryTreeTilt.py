# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        self.re = 0
        def com(root):
            l = 0
            r = 0
            if root.left:
                l = com(root.left)
            if root.right:
                r = com(root.right)
            self.re += abs(l - r)
            return l + r + root.val
        if root:
            com(root)
        return self.re
