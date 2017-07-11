class MedianFinder(object):

    def __init__(self):
        self.left = [float('inf')]
        self.right = [float('inf')]
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        heapq.heappush(self.right, num)
        temp = heapq.heappop(self.right)
        heapq.heappush(self.left, -temp)
        if len(self.left) > len(self.right):
            temp = -heapq.heappop(self.left)
            heapq.heappush(self.right, temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.left) == len(self.right):
            return (-self.left[0] + self.right[0]) / 2.0
        else:
            return self.right[0] * 1.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
