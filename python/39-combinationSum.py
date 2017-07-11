class Solution(object):
    def combinationSum(self, candidates, target):
        cands = list(candidates)
        cands.sort(reverse = True)
        res = []
        def search(pos, temp):
            if pos == len(cands): 
                if sum(temp) == target:
                    res.append(temp)
            else:
                left = target - sum(temp)
                for i in range(0, left / cands[pos] + 1):
                    search(pos + 1, temp + [cands[pos]] * i)
        search(0, [])
        return res
