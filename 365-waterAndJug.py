class Solution(object):
    def canMeasureWater(self, x, y, z):
        if x + y < z:
            return False
        if x == 0 or y == 0:
            return z == x or z == y
        a, b = x, y
        while a % b != 0:
            a, b = b, a % b
        return z % b == 0
