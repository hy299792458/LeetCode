# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        self.find = [None, None]
        self.win = []
        def check(node):
            self.win.append(node)
            if len(self.win) >= 3:
                self.win = self.win[-3:]
                if self.win[1].val > max(self.win[0].val, self.win[2].val) and not(self.find[0]):
                    self.find[0] = self.win[1]
                if self.win[1].val < min(self.win[0].val, self.win[2].val):
                    self.find[1] = self.win[1]
        check(TreeNode(-float('inf')))
        while root:
            if root.left:
                pre = root.left
                while pre.right and pre.right != root:
                    pre = pre.right
                if pre.right:
                    pre.right = None
                    check(root)
                    root = root.right
                else:
                    pre.right = root
                    root = root.left
            else:
                check(root)
                root = root.right
        check(TreeNode(float('inf')))
        if self.find[0] and self.find[1]:
            self.find[0].val, self.find[1].val = self.find[1].val, self.find[0].val