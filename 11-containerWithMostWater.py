class Solution(object):
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            res = max(res, h * (r - l))
            while l < len(height) and height[l] <= h:
                l += 1
            while r >= 0 and height[r] <= h:
                r -= 1
        return res
