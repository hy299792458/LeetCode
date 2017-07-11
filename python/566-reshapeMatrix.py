class Solution(object):
    def matrixReshape(self, nums, r, c):
        x, y = len(nums), len(nums[0])
        if r * c != x * y:
            return nums
        re = []
        line = []
        for l in nums:
            for num in l:
                line.append(num)
                if len(line) == c:
                    re.append(line[:])
                    line = []
        return re
