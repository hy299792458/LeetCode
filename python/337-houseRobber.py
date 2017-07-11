# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#Slow solution use dic for DP
class Solution(object):
    seen = {}
    def rob(self, root):
        if root in self.seen:
            return self.seen[root]
        v1 = v2 = 0
        if root:
            v1 += root.val
            if root.left:
                v2 += self.rob(root.left)
                if root.left.left:
                    v1 += self.rob(root.left.left)
                if root.left.right:
                    v1 += self.rob(root.left.right)
            if root.right:
                v2 += self.rob(root.right)
                if root.right.left:
                    v1 += self.rob(root.right.left)
                if root.right.right:
                    v1 += self.rob(root.right.right)
        self.seen[root] = max(v1, v2)
        return self.seen[root]

class Solution(object):
    def rob(self, root):
        return self.robDFS(root)[1]

    def robDFS(self,node):
        if node is None:
            return (0,0)
        l = self.robDFS(node.left)
        r = self.robDFS(node.right)
        return (l[1] + r[1], max(l[1] + r[1], l[0] + r[0] + node.val))
