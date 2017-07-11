class Solution(object):
    def topKFrequent(self, nums, k):
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        re = [num for num in set(nums)]
        re.sort(key = lambda x: -count[x])
        return re[:k]
