# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        res = []
        if not root:
            return res
        level = [root]
        while level:
            res.append(level[-1].val)
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
        return res 
