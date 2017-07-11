class Solution(object):
    def findLongestWord(self, s, d):
        def check(word):
            iterd= iter(s)
            return all(char in iterd for char in word)
        cand = filter(check, d)
        res = ["", 0]
        for l in cand:
            if len(l) > res[1]:
                res = [l, len(l)]
            elif len(l) == res[1]:
                res[0] = min(res[0], l)
        return res[0]
