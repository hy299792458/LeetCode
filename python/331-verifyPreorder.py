class Solution(object):
    def isValidSerialization(self, preorder):
        if not preorder:
            return False
        preorder = preorder.split(",")
        level = [preorder[0]]
        s = 1
        while any(n != "#" for n in level):
            #print level
            cnt = sum(2 for n in level if n != "#")
            if s + cnt > len(preorder):
                return False
            level = preorder[s: s + cnt]
            s += cnt
        return s == len(preorder)
