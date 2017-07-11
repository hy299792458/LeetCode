# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        dirct = -1
        if not root:
            return []
        level = [root]
        res = [[root.val]]
        while level:
            vals = []
            nextLevel = []
            for node in level:
                if node.left:
                    nextLevel.append(node.left)
                    vals.append(node.left.val)
                if node.right:
                    nextLevel.append(node.right)
                    vals.append(node.right.val)
            level = nextLevel
            res.append(vals[::dirct])
            dirct *= -1
        return res[:-1]
