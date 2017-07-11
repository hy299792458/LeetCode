# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        self.res = -float('inf')
        def search(root, s):
            if s == None:
                temp = root.val
            else:
                temp = max(root.val, s + root.val)
            l = r = -float('inf')
            if root.left:
                l = search(root.left, temp)
            if root.right:
                r = search(root.right, temp)
            self.res = max(l + r + root.val, l + temp, temp + r, temp, self.res)
            return max(l, r, 0) + root.val
        if root:
            search(root, None)
        return self.res
