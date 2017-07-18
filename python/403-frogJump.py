class Solution(object):
    def canCross(self, stones):
        target = max(stones)
        stones = set(stones)
        cache = {}
        def dfs(pos, jump):
            if (pos, jump) in cache:
                return cache[(pos, jump)]
            if pos == target:
                res = True
            elif pos > target or pos not in stones:
                res = False
            else:
                if jump == 1:
                    cand = [1, 2]
                else:
                    cand = [jump, jump + 1, jump - 1]
                res = any(dfs(pos + j, j) for j in cand)
            cache[(pos, jump)] = res
            return res
        return dfs(1, 1)
