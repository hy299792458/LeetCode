class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        re = [[]]
        for num in nums:
            app = []
            for l in re:
                app.append(l + [num])
            re += app
        return re
