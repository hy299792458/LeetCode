class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            dig = []
            while n:
                dig.append(n % 10)
                n /= 10
            n = sum(num ** 2 for num in dig)
        return True
