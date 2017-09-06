# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        path = collections.defaultdict(list)
        def dfs(root):
            if not root:
                return [None]
            else:
                l = dfs(root.left)
                r = dfs(root.right)
                temp = [root.val] + l + r
                path[tuple(temp)].append(root)
                return temp
        dfs(root)
        res = []
        for k in path:
            if len(path[k]) > 1:
                res.append(path[k][0])
        return res
