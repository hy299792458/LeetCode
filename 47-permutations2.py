class Solution(object):
    def permuteUnique(self, nums):
        res = []
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        vals = count.keys()
        cnts = count.values()
        def dfs(temp, count):
            if count == cnts:
                res.append(temp)
            else:
                for i in range(len(cnts)):
                    if count[i] < cnts[i]:
                        cnt = count[:]
                        cnt[i] += 1
                        dfs(temp + [vals[i]], cnt)
        dfs([], [0 for _ in cnts])
        return res
