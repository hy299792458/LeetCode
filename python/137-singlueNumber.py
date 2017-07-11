class Solution(object):
    def singleNumber(self, nums):
        a , b = 0, 0 
        for num in nums:
            a, b = (a & ~num) | (num & ~a & b) , (b ^ num) & ~a
        return b
