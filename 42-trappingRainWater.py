class Solution(object):
    def trap(self, height):
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            h = min(height[l], height[r])
            while l < r and height[l] <= h:
                res += h - height[l]
                l += 1
            while r> l and height[r] <= h:
                res += h - height[r]
                r -= 1
        return res
