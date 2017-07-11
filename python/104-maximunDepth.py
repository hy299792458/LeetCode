# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        depth = 0
        level = [root]
        while True:
            newLevel = []
            for node in level:
                if node:
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            if newLevel:
                depth += 1
            else:
                return depth
            level = newLevel
