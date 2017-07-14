class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        end = len(matrix[0])
        for row in matrix:
            start = 0
            while start < end:
                mid = (start + end) / 2
                if row[mid] < target:
                    start = mid + 1
                elif row[mid] > target:
                    end = mid
                else:
                    return True
        return False
