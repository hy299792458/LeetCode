# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        self.res = None
        def search(root):
            l, r = False, False
            l1 = l2 = r1 = r2 = False
            if root == p:
                l = True
            if root == q:
                r = True
            if root.left:
                l1, r1 = search(root.left)
            if root.right:
                l2, r2 = search(root.right)
            l = l or l1 or l2
            r = r or r1 or r2
            if l and r and self.res == None:
                self.res = root
            return l, r
        search(root)
        return self.res
