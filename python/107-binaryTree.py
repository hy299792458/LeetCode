# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        res = []
        level = [root]
        while level:
            newLevel = []
            value = []
            for node in level:
                if node:
                    value.append(node.val)
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            level = newLevel
            res.append(value[:])
        res.pop()
        return res[::-1]
