# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        self.res = [0, []]
        self.temp = [0, 0]
        def search(root):
            if root.left:
                search(root.left)
            if self.temp[1] == root.val:
                self.temp[0] += 1
            else:
                if self.res[0] == self.temp[0]:
                    self.res[1].append(self.temp[1])
                elif self.res[0] < self.temp[0]:
                    self.res = [self.temp[0], [self.temp[1]]]
                self.temp = [1, root.val]
            if root.right:
                search(root.right)
        if root:
            search(root)
        if self.res[0] == self.temp[0]:
            self.res[1].append(self.temp[1])
        elif self.res[0] < self.temp[0]:
            self.res = [self.temp[0], [self.temp[1]]]
        return self.res[1]
