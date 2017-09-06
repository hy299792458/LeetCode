# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        def add(root, v, d, ad):
            if ad == d:
                    temp = TreeNode(v)
                    temp.left = root.left
                    root.left = temp
                    temp = TreeNode(v)
                    temp.right = root.right
                    root.right = temp
            else:
                if root.left:
                    add(root.left, v, d + 1, ad)
                if root.right:
                    add(root.right, v, d + 1, ad)
        start = TreeNode(0)
        start.left = root
        add(start, v, 1, d)
        return start.left
