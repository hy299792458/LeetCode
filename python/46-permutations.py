class Solution(object):
    def permute(self, nums):
        res = []
        nums = set(nums)
        def dfs(temp, used):
            if len(used) == len(nums):
                res.append(temp)
            else:
                for num in nums:
                    if num not in used:
                        dfs(temp + [num], used |{num})
        dfs([], set())
        return res
