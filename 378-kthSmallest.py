class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = [(matrix[0][0], 0, 0)]
        l = len(matrix)
        for _ in range(k):
            res, x, y = heapq.heappop(heap)
            #print res, x, y
            if x + 1 < l and matrix[x + 1][y] != None:
                heapq.heappush(heap, (matrix[x + 1][y], x + 1, y))
                matrix[x + 1][y] = None
            if y + 1 < l and matrix[x][y + 1] != None:
                heapq.heappush(heap, (matrix[x][y + 1], x, y + 1))
                matrix[x][y + 1] = None
            #print heap
        return res
