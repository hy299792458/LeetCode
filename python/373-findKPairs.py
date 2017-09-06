class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        res = []
        heap = []
        for n in nums1:
            heapq.heappush(heap, (n + nums2[0], 0))
        for _ in range(min(k, len(nums1) * len(nums2))):
            total, p = heapq.heappop(heap)
            res.append([total - nums2[p], nums2[p]])
            if p + 1 < len(nums2):
                heapq.heappush(heap, (total - nums2[p] + nums2[p + 1], p + 1))
        return res
