# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        res = []
        def search(path, root):
            path += [root.val]
            if root.left:
                search(path[:], root.left)
            if root.right:
                search(path[:], root.right)
            if not root.left and not root.right:
                if sum(path) == target:
                    res.append(path)
        if root:
            search([], root)
        return res
