# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        level = [root]
        res = []
        while level:
            newLevel = []
            cnt = 0
            tal = 0
            for node in level:
                cnt += 1
                tal += node.val
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            res.append(tal * 1.0 / cnt)
            level = newLevel
        return res
