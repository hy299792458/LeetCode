class Solution(object):
    def minCut(self, s):
        if not s:
            return 0
        ends = {0}
        seen = {0}
        cnt = -1
        def check(s):
            return s == s[::-1]
        while len(s) not in ends:
            newEnds = set()
            for e in ends:
                for i in range(e + 1, len(s) + 1):
                    if i not in seen and check(s[e: i]):
                        newEnds.add(i)
            ends = newEnds
            seen |= ends
            cnt += 1
        return cnt