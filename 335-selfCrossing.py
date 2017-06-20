class Solution(object):
    def isSelfCrossing(self, x):
        if len(x) < 4:
            return False
        x += [0, 0]
        a, b, c, d, e, f = x[: 6]
        i = 6
        while True:
            if a >= c and d >= b:
                print a, b, c, d
                return True
            if a <= c and e <= c and a + e >= c \
            and b <= d and f <= d and b + f >= d:
                print a, b, c, d, e, f
                return True
            if i == len(x):
                return False
            a, b, c, d, e, f = b, c, d, e, f, x[i]
            i += 1
