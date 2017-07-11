class NumArray(object):

    def __init__(self, nums):
        self.nums = nums
        for i in range(1, len(nums)):
            self.nums[i] += self.nums[i - 1]
        

    def sumRange(self, i, j):
        if i == 0:
            return self.nums[j]
        else:
            return self.nums[j] - self.nums[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
