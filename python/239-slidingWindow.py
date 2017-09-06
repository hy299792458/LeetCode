class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if k <= 1:
            return nums

        res = []
        heap = []
        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        for i in range(k - 1, len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            while heap[0][1] + k <= i:
                heapq.heappop(heap)
            res.append(-heap[0][0])
        return res
