# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.re = 1
        def search(root):
            l = r = 0
            if root.left:
                l = search(root.left)
            if root.right:
                r = search(root.right)
            self.re = max(self.re, l + r + 1)
            return max(l, r) + 1
        if root:
            search(root)
        return self.re - 1
