# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        if not root:
            return []
        res = []
        level = [root]
        while level:
            newLevel = []
            maxVal = -float('inf')
            for node in level:
                maxVal = max(maxVal, node.val)
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
            res.append(maxVal)
        return res
