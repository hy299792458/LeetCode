class Solution(object):
    def judgeSquareSum(self, c):
        if c == 0:
            return True
        for i in range(1, int(math.sqrt(c) + 1)):
            if math.sqrt(c - i * i) % 1 == 0:
                return True
        return False
