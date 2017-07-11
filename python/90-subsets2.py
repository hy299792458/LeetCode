class Solution(object):
    def subsetsWithDup(self, nums):
        cnt = collections.Counter(nums)
        res = [[]]
        for k in sorted(cnt.keys()):
            toAdd = []
            for l in res:
                for i in range(cnt[k]):
                    toAdd.append(l + (i + 1) * [k])
            res += toAdd
        return res
