# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        self.res = True
        def check(root):
            l = [None, None]
            r = [None, None]
            if root.left:
                l = check(root.left)
                if root.val <= l[1]:
                    self.res = False
            if root.right:
                r = check(root.right)
                if root.val >= r[0]:
                    self.res = False
            l = min(l[0], root.val) if l[0] != None else root.val
            r = max(r[1], root.val) if r[1] != None else root.val
            return [l, r]
        if root:
            check(root)
        return self.res
            
