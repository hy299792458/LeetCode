# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        re = set()
        level = [root]
        while level:
            newLevel = []
            for node in level:
                if node:
                    re.add(node.val)
                    newLevel += [node.left, node.right]
            level = newLevel
        re = list(re)
        re.sort()
        diff = float('inf')
        for i in range(len(re) - 1):
            diff = min(re[i + 1] - re[i], diff)
        return diff
