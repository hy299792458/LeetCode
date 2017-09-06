class Solution(object):
    def findMaximizedCapital(self, k, W, Profits, Capital):
        projs = sorted(zip(Capital, Profits))
        cands = []
        pos = 0
        for _ in range(k):
            while pos < len(projs) and projs[pos][0] <= W:
                heapq.heappush(cands, -projs[pos][1])
                pos += 1
            if cands:
                W -= heapq.heappop(cands)
        return W
