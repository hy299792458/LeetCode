class Solution(object):
    def lexicalOrder(self, n):
        l = int(math.log(n, 10))
        bar = 10 ** l
        def cmp(a):
            while a < bar:
                a *= 10
            return a
        return sorted(xrange(1, n + 1), key = cmp)
