# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        level = [root]
        while any(type(node) != int for node in level):
            newLevel = []
            for node in level:
                if type(node) == int:
                    newLevel.append(node)
                else:
                    if node.left:
                        newLevel.append(node.left)
                    if node.right:
                        newLevel.append(node.right)
                    newLevel.append(node.val)
            level = newLevel
        return level
