class Solution(object):
    def findAnagrams(self, s, p):
        res = []
        if len(s) < len(p):
            return res
        target = {}
        for char in p:
            target[char] = target.get(char, 0) + 1
        l = r = 0
        for r in range(len(p)):
            if s[r] in target:
                target[s[r]] -= 1
        if all(val == 0 for val in target.values()):
            res.append(0)
        r = len(p)
        while r < len(s):
            if s[r] in target:
                target[s[r]] -= 1
            r += 1
            if s[l] in target:
                target[s[l]] += 1
            l += 1
            if all(val == 0 for val in target.values()):
                res.append(l)
        return res
        
