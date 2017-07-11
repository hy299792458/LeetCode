class Solution(object):
#O(n^3) solution without optimaization, it's slow but it works
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = len(nums) - 1
                aim = target - nums[i] - nums[j]
                while l < len(nums) and r > j and l < r:
                    if nums[l] + nums[r] < aim:
                        l += 1
                    elif nums[l] + nums[r] > aim:
                        r -= 1
                    else:
                        left = nums[l]
                        right = nums[r]
                        #print i, j, l, r
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < len(nums) and nums[l] == left:
                            l += 1
                        while r > j and nums[r] == right:
                            r -= 1
        return res
