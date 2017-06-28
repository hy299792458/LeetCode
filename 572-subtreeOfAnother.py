# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        def match(t1, t2):
            if t1 == None:
                if t2 != None:
                    return False
                return True
            else:
                if t2 == None or t2.val != t1.val:
                    return False
                else:
                    l1 = match(t1.left, t2.left)
                    l2 = match(t1.right, t2.right)
                    return l1 and l2
        level = [s]
        while level:
            newLevel = []
            for node in level:
                if node:
                    newLevel.append(node.left)
                    newLevel.append(node.right)
                    if node.val == t.val:
                        if match(node, t):
                            return True
            level = newLevel
        return False
