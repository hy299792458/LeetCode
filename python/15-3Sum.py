class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        l = len(nums)
        re = []
        numSet = set(nums)
        for i in xrange(l - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = l - 1
            while left < right:
                if nums[left] + nums[right] < -nums[i]:
                    left += 1
                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1
                else:
                    re.append((nums[i], nums[left], nums[right]))
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return re
