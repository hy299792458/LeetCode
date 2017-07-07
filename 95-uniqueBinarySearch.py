# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        def genSub(l, r):
            if r <= l:
                return [None]
            res = []
            for i in range(l, r):
                left = genSub(l, i)
                right = genSub(i + 1, r)
                for lNode in left:
                    for rNode in right:
                        root = TreeNode(i)
                        root.left = lNode
                        root.right = rNode
                        res.append(root)
            return res
        if n <= 0:
            return []
        return genSub(1, n + 1)
