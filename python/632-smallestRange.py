class Solution(object):
    def smallestRange(self, nums):
        heap = [(nums[i][0], i, 0) for i in range(len(nums))]
        heapq.heapify(heap)
        maxVal = max(heap)[0]
        minVal = min(heap)[0]
        res = [minVal, maxVal]
        while True:
            #print heap
            temp, order, position = heapq.heappop(heap)
            try:
                temp = nums[order][position + 1]
                heapq.heappush(heap, (temp, order, position + 1))
                maxVal = max(maxVal, temp)
                minVal = heap[0][0]
                if maxVal - minVal < res[1] - res[0]:
                    res = [minVal, maxVal]

            except:
                return res
        return res
