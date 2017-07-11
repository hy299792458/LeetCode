# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(line):
            l = 0
            r = len(line) - 1
            while l <= r:
                if line[l] == line[r] == None:
                    l += 1
                    r -= 1
                elif line[l] == None or line[r] == None:
                    return False
                else:
                    if line[l].val != line[r].val:
                        return False
                    l += 1
                    r -= 1
            return True
        level = [root]
        while level:
            newLevel = []
            for node in level:
                if node:
                    newLevel.append(node.left)
                    newLevel.append(node.right)
            if not check(newLevel):
                return False
            else:
                level = newLevel
        return True
                    
