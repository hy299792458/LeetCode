class Solution(object):
    def findMaxLength(self, nums):
        store = {0: -1}
        count = 0
        res = 0
        for i in range(len(nums)):
            if nums[i]:
                count += 1
            else:
                count -= 1
            if count in store:
                res = max(i - store[count], res)
            else:
                store[count] = i
        return res
