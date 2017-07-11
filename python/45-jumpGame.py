class Solution(object):
    def jump(self, nums):
        r = 1
        l = 0
        count = 0
        while r < len(nums):
            temp = r
            for i in range(l, r):
                temp = max(nums[i] + i, temp)
            l = r
            r = temp + 1
            count += 1
        return count
                
