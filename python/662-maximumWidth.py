# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        slevel = {}
        blevel = {}
        def bfs(root, cnt, depth):
            if root:
                slevel[depth] = min(slevel.get(depth, float('inf')), cnt)
                blevel[depth] = max(blevel.get(depth, -float('inf')), cnt)
                bfs(root.left, cnt * 2, depth + 1)
                bfs(root.right, cnt * 2 + 1, depth + 1)
        bfs(root, 0, 0)
        res = 0
        dep = 0
        while dep in slevel:
            res = max(res, blevel[dep] - slevel[dep] + 1)
            dep += 1
        return res
