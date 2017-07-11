# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        depth = 1
        if not root:
            return 0
        level = [root]
        while level:
            if any(node.left == node.right == None for node in level):
                return depth
            newLevel = []
            for node in level:
                if node.left:
                    newLevel.append(node.left)
                if node.right:
                    newLevel.append(node.right)
            level = newLevel
            depth += 1
