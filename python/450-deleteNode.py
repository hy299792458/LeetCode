# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        self.find = []
        def search(root, c, p):
            if root.val == key:
                self.find = [p, c]
            else:
                if root.left:
                    search(root.left, "l", root)
                if root.right:
                    search(root.right, "r", root)
        pre = TreeNode(None)
        pre.left = root
        search(pre, "l", pre)
        if not self.find:
            return pre.left
        find = self.find
        if find[1] == "l":
            r = find[0].left.right
            l = find[0].left.left
            if not r or not l:
                find[0].left = l or r
            else:
                find[0].left = l
                while l.right:
                    l = l.right
                l.right = r
        else:
            r = find[0].right.right
            l = find[0].right.left
            if not l or not r:
                find[0].right = r or l
            else:
                find[0].right = r
                while r.left:
                    r = r.left
                r.left = l
        return pre.left
