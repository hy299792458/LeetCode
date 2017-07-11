class Solution(object):
    def nextGreaterElements(self, nums):
        stack = []
        res = [-1 for _ in nums]
        for i in range(2 * len(nums)):
            p = i % len(nums)
            num = nums[p]
            while stack and stack[-1][1] < num:
                lp, lnum = stack.pop()
                if res[lp] == -1:
                    res[lp] = num
            stack.append((p, num))
        return res
