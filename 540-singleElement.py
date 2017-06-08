class Solution(object):
    def singleNonDuplicate(self, nums):
        return reduce(lambda x, y: x^y, nums)
