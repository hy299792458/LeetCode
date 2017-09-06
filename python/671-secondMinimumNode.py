# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        self.res = []
        def check(root):
            if root.left:
                check(root.left)
            self.res.append(root.val)
            if root.right:
                check(root.right)
        if root:
            check(root)
        self.res.sort()
        if not self.res or self.res[0] == self.res[-1]:
            return -1
        print self.res
        for num in self.res:
            if num > self.res[0]:
                return num
