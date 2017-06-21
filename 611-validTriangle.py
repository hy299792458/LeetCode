class Solution(object):
    def triangleNumber(self, nums):
        re = 0
        def check(a, b, c):
            if a + b > c:
                return True
            return False
        nums.sort()
        #print nums
        for i in xrange(len(nums)):
            k = 2
            for j in xrange(i + 1,len(nums)):
                while k < len(nums) and check(nums[i], nums[j], nums[k]):
                    k += 1
                #print i, j, k
                if k - j - 1 > 0:
                    re += (k - j - 1)
        return re
