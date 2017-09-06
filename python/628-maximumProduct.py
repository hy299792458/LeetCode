class Solution(object):
    def maximumProduct(self, nums):
        nums.sort()
        def pro(num):
            re = 1
            for n in num:
                re *= n
            return re
        t1 = pro(nums[:3])
        t2 = pro(nums[:2] + nums[-1:])
        t3 = pro(nums[:1] + nums[-2:])
        t4 = pro(nums[-3:])
        return max(t1, t2, t3, t4)
