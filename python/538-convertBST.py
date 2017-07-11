# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def convertBST(self, root):
        def search(root, val):
            temp = val
            if root.right:
                val += search(root.right, val)
            val += root.val
            root.val = val
            if root.left:
                val += search(root.left, val)
            return val - temp
        if root:
            search(root, 0)
        return root
