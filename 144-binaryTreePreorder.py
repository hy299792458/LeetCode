# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        if not root:
            return []
        level = [root]
        while any(type(node) == TreeNode for node in level):
            temp = []
            for node in level:
                if type(node) == TreeNode:
                    temp.append(node.val)
                    if node.left:
                        temp.append(node.left)
                    if node.right:
                        temp.append(node.right)
                else:
                    temp.append(node)
            level = temp
        return level
