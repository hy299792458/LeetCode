# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def tree2str(self, t):
        def search(root):
            re = ''
            if root == None:
                return ''
            else:
                re += str(root.val)
                if root.left:
                    re += '(' + search(root.left) + ')'
                    if root.right:
                        re += '(' + search(root.right) + ')'
                elif root.right:
                    re += '()'
                    re += '(' + search(root.right) + ')'
                return re
        return search(t)
