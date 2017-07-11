class Solution(object):
    def largestDivisibleSubset(self, nums):
        nums.sort()
        store = {-1: set()}
        for num in nums:
            store[num] = max((store[k] for k in store if num % k == 0), key = len) | {num}
        return list(max((store[k] for k in store), key = len))
