class Solution(object):
    def singleNumber(self, nums):
        diff = reduce(lambda x, y: x ^ y, nums)
        thr = diff & ~(diff - 1)
        g1 = g2 = 0
        for num in nums:
            if num & thr > 0:
                g1 ^= num
            else:
                g2 ^= num
        return [g1, g2]
