class Solution(object):
    def nextPermutation(self, nums):
        p = len(nums) - 2
        while p >= 0:
            if nums[p] < nums[p + 1]:
                temp = min(num for num in nums[p:] if num > nums[p])
                index = nums[p:].index(temp)
                nums[p], nums[p + index] = temp, nums[p]
                nums[p + 1:] = sorted(nums[p + 1:])
                return
            p -= 1
        nums[:] = nums[::-1]
        return 
