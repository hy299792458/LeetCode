class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        t, d = 0, len(matrix)
        while True:
            if d <= t + 1:
                break
            mid = (t + d) / 2
            if matrix[mid][0] < target:
                t = mid
            elif matrix[mid][0] > target:
                d = mid
            else:
                return True
        line = matrix[t]
        l, r = 0, len(line)
        while True:
            if r <= l + 1:
                break
            mid = (l + r) / 2
            if line[mid] < target:
                l = mid
            elif line[mid] > target:
                r = mid
            else:
                return True
        return line[l] == target
