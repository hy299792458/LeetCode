class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        l1, l2 = len(g), len(s)
        re = p1 = p2 = 0
        while p1 < l1 and p2 < l2:
            if g[p1] <= s[p2]:
                re += 1
                p1 += 1
            p2 += 1
        return re    
