# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        def search(root):
            if not root or root in (p, q):
                return root
            l = search(root.left)
            r = search(root.right)
            return root if l and r else l or r
        return search(root)
