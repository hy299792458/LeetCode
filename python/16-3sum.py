class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        res = float('inf')
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                temp = nums[l] + nums[r] + nums[i]
                if temp > target:
                    r -= 1
                else:
                    l += 1
                if abs(temp - target) < abs(res - target):
                    res = temp
        return res
