class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        re = set()
        def DFS(temp, pos, toadd):
            if toadd == 0:
                re.add(tuple(temp))
            else:
                pos += 1
                cand = None
                while pos < len(candidates) and candidates[pos] <= toadd:
                    cand = candidates[pos] 
                    DFS(temp + [cand], pos, toadd - cand)
                    pos += 1
        DFS([], -1, target)
        return list(re)
