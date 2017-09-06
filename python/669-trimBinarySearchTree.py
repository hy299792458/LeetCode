# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        def check(root):
            if not root:
                return None
            if root.val >= L and root.val <= R:
                root.left = check(root.left)
                root.right = check(root.right)
                return root
            if root.val > R:
                return check(root.left)
            if root.val < L:
                return check(root.right)
        return check(root)
