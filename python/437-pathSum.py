# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        self.res = 0
        def search(root, path):
            newPath = [root.val]
            for val in path:
                newPath.append(val + root.val)
            self.res += sum(1 for num in newPath if num == target)
            if root.left:
                search(root.left, newPath)
            if root.right:
                search(root.right, newPath)
        if root:
            search(root, [])
        return self.res
