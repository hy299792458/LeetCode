class Solution(object):
    def findRepeatedDnaSequences(self, s):
        temp = 0
        if len(s) < 10:
            return []
        l = r = 0
        mapping = {'A' : 0, 'T' : 1, 'C' : 2, 'G' : 3}
        while r < 10:
            temp *= 4
            temp += mapping[s[r]]
            r += 1
        res = set()
        seen = set([temp])
        mod = (1 << 20) - 1
        while r < len(s):
            temp *= 4
            temp = temp & mod
            temp += mapping[s[r]]
            #print bin(temp)
            if temp in seen:
                res.add(s[r - 9 : r + 1])
            else:
                seen.add(temp)
            r += 1
        return list(res)
