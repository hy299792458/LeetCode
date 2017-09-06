# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree(self, root):
        self.depth = 0
        level = [root]
        while any(node for node in level):
            new = []
            for node in level:
                if node:
                    new += [node.left, node.right]
            self.depth += 1
            level = new    
        def build(root, level):
            if root:
                level -= 1
                res = [[""] * (2 ** level - 1) + [str(root.val)] + [""] * (2 ** level - 1)]
                if level:
                    left = build(root.left, level)
                    right = build(root.right, level)
                    for i in range(max(len(left), len(right))):
                        temp = []
                        temp += left[i] if i < len(left) else [""] * len(left[0])
                        temp += [""]
                        temp += right[i] if i < len(right) else [""] * len(right[0])
                        res.append(temp)
                return res
            else:
                return [[""] * (2 ** level - 1)]
        if root:
            return build(root, self.depth)
        return []
