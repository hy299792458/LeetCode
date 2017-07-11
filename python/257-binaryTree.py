# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        self.re = []
        def DFS(root,path):
            if root.left == root.right == None:
                self.re.append(path + [root.val])
            else:
                if root.left:
                    DFS(root.left, path + [root.val])
                if root.right:
                    DFS(root.right, path + [root.val])
        if root:
            DFS(root, [])
        return map(lambda x: '->'.join(map(str, x)), self.re)
