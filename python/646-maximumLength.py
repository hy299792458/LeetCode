class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x : x[1])
        end = pairs[0][1]
        cnt = 1
        for p in pairs[1:]:
            if p[0] > end:
                end = p[1]
                cnt += 1
        return cnt
