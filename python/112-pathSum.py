# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, target):
        self.res = False
        def search(root, temp):
            temp += root.val
            if root.left:
                search(root.left, temp)
            if root.right:
                search(root.right, temp)
            if not (root.left or root.right):
                if temp == target:
                    self.res = True
        if root:
            search(root, 0)
        return self.res 
