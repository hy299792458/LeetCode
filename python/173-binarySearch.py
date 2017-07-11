# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        self.tree = []
        def search(root):
            if root.left:
                search(root.left)
            self.tree.append(root.val)
            if root.right:
                search(root.right)
        if root:
            search(root)
        self.p = 0
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.p < len(self.tree)

    def next(self):
        """
        :rtype: int
        """
        re = self.tree[self.p]
        self.p += 1
        return re

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
