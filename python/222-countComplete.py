# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        l = r = 1
        left = root.left
        right = root.right
        while left:
            l += 1
            left = left.left
        while right:
            r += 1
            right = right.right
        if l == r:
            return 2 ** l - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
