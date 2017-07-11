class Solution(object):
    def checkRecord(self, n):
        mod = 10 ** 9 + 7
        temp = [1, 0, 0, 0, 1, 0, 1]
        for _ in xrange(n - 1):
            temp = [(temp[4] + temp[5] + temp[6]) % mod,\
                    (temp[3] + temp[0]) % mod,\
                    temp[1],\
                    (temp[0] + temp[1] + temp[2] + temp[3]) % mod,\
                    temp[6],\
                    temp[4],\
                    (temp[4] + temp[5] + temp[6]) % mod]
        return sum(temp) % mod
