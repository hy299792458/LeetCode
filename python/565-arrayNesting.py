class Solution(object):
    def arrayNesting(self, nums):
        re = 0
        length = len(nums)
        seen = set()
        for i in xrange(length):
            if nums[i] not in seen:
                num = nums[i]
                count = 0
                while nums[num] not in seen:
                    
                    seen.add(nums[num])
                    num = nums[num]
                    count += 1
                re = max(re, count)
                if re > length / 2:
                    return re
        return re
