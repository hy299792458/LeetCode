# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        self.res = {}
        def search(root):
            l = r = 0
            if root.left:
                l = search(root.left)
            if root.right:
                r = search(root.right)
            total = l + r + root.val
            self.res[total] = self.res.get(total, 0) + 1
            return total
        if not root:
            return []
        search(root)
        maxVal = max(self.res.values() + [0])
        return [k for k in self.res if self.res[k] == maxVal]
