# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        self.res = None
        self.k = k
        def search(root):
            if self.k > 0:
                if root.left:
                    search(root.left)
                self.k -= 1
                if self.k == 0:
                    self.res = root.val
                if root.right:
                    search(root.right)
        search(root)
        return self.res
        
