class Solution(object):
    def findRelativeRanks(self, nums):
        re = nums[:]
        nums.sort(reverse = True)
        order = dict(zip(nums[:], \
        ["Gold Medal", "Silver Medal", "Bronze Medal"]\
        + [str(i + 1) for i in range(3, len(nums))]))
        return map(lambda x: order.get(x), re)
