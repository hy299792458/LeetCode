class Solution(object):
    def findKthLargest(self, nums, k):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res
        
