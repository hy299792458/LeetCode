# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        def invert(root):
            if root:
                root.left, root.right = root.right, root.left
                invert(root.left)
                invert(root.right)
        invert(root)
        return root
