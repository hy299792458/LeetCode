class Solution(object):
    def integerBreak(self, n):
        store = {}
        def div(num):
            if num in store:
                return store[num]
            re = num
            for i in range(1,num):
                re = max(re, div(i) * div(num - i))
            store[num] = re
            return re
        re = 0
        for i in range(1, n):
            re = max(re, div(i) * div(n - i))
        return re
