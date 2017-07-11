class Solution(object):
    def largestRectangleArea(self, heights):
        stack = [(-1, -1)]   #height, position, the last one is set to be zero
        area = 0
        for p, h in enumerate(heights + [0]):
            if h <= stack[-1][0]:
                height, pos = stack.pop()
                while h <= stack[-1][0]:
                    th, tp = stack.pop()
                    area = max(area, height * (p - tp - 1))
                    height = min(th, height)
                area = max(area, height * (p - stack[-1][1] - 1))
            stack.append((h, p))
        return area
