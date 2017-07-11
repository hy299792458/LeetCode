class Solution(object):
    def findDuplicates(self, nums):
        for num in nums:
            nums[int(abs(num) - 1)] = - float(nums[int(abs(num) - 1)])
        re = []
        #print nums
        for i in range(len(nums)):
            if nums[i] > 0 and type(nums[i]) == float:
                re.append(i + 1)
        return re
