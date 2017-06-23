class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        re = 0
        for _ in range(32):
            re *= 2
            re += n % 2
            n /= 2
        return re
