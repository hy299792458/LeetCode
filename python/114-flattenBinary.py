# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    tail = root = TreeNode(0)
    def flatten(self, root):
        if not root:
            return 
        left = root.left
        right = root.right
        self.tail.right = root
        self.tail = root
        self.tail.left = None
        self.flatten(left)
        self.flatten(right)
