# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        self.re = True
        def check(root):
            l = -1
            r = -1
            if root.left:
                l = check(root.left)
            if root.right:
                r = check(root.right)
            if abs(l - r) <= 1:
                return max(l, r) + 1
            else:
                self.re = False
                return 0
        if root:
            check(root)
        return self.re
