class NumArray(object):

    def __init__(self, nums):
        self.res = [nums]
        self.l = 1
        while len(nums) > 1:
            nums = [a + b for a, b in zip(nums[::2], nums[1::2] + [0])]
            self.res.append(nums)
            self.l += 1

    def update(self, i, val):
        add = val - self.res[0][i]
        for k in range(self.l):
            self.res[k][i] += add
            i /= 2

    def sumRange(self, i, j):
        res = self.res[-1][0]
        for k in range(self.l):
            if i % 2 == 1:
                res -= self.res[k][i - 1]
            i /= 2
        for k in range(self.l):
            if j % 2 == 0 and j + 1 < len(self.res[k]):
                res -= self.res[k][j + 1]
            j /= 2
        return res
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
