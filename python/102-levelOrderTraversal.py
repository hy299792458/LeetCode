# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        res = []
        temp = [root]
        while temp:
            sigRes = []
            newTemp = []
            for node in temp:
                if node:
                    sigRes.append(node.val)
                    newTemp.append(node.left)
                    newTemp.append(node.right)
            if sigRes:
                res.append(sigRes[:])
            temp = newTemp
        return res