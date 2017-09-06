class Solution(object):
    def checkPossibility(self, nums):
        def check(nums):
            #print nums
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return check(nums[:i]+ nums[i+1:]) or check(nums[: i+ 1] + nums[i + 2:])
        return True
