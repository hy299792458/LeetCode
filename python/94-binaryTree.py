# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        level = [root]
        while any(type(node) == TreeNode for node in level):
            newLevel = []
            for node in level:
                if type(node) == TreeNode:
                    if node.left:
                        newLevel.append(node.left)
                    newLevel.append(node.val)
                    if node.right:
                        newLevel.append(node.right)
                else:
                    newLevel.append(node)
            level = newLevel
        return level
