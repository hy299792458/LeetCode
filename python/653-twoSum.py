# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        seen = set()
        self.res = False
        def search(root):
            if self.res:
                return
            if root.left:
                search(root.left)
            if k - root.val in seen:
                self.res = True
                return 
            seen.add(root.val)
            if root.right:
                search(root.right)
        if root:
            search(root)
        return self.res
