class Solution(object):
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        res = 0
        temp = [0 for _ in matrix[0]]
        for i in range(len(matrix)):
            newTemp = []
            for a, b in zip(temp, list(matrix[i])):
                if b == '0':
                    newTemp.append(0)
                else:
                    newTemp.append(a + int(b))
            temp = newTemp
            stack = [(-1, -1)]   #height, position, the last one is set to be zero
            area = 0
            for p, h in enumerate(temp + [0]):
                if h <= stack[-1][0]:
                    height, pos = stack.pop()
                    while h <= stack[-1][0]:
                        th, tp = stack.pop()
                        area = max(area, height * (p - tp - 1))
                        height = min(th, height)
                    area = max(area, height * (p - stack[-1][1] - 1))
                stack.append((h, p))
            res = max(res, area)
        return res
        
