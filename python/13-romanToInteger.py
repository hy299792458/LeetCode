class Solution(object):
    def romanToInt(self, s):
        trans = {'M': 1000, 'D': 500, 'C': 100, "L": 50, "X": 10, "V": 5, "I": 1}
        res = 0
        for i in range(len(s) - 1):
            if trans[s[i]] >= trans[s[i + 1]]:
                res += trans[s[i]]
            else:
                res -= trans[s[i]]
        res += trans[s[-1]]
        return res
