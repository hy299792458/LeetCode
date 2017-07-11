class Solution(object):
    def checkPerfectNumber(self, num):
        if num <= 1:
            return False
        factor = set([1])
        for i in range(2, int(math.sqrt(num)) + 1):
            while num % i == 0:
                factor.add(i)
                factor.add(num / i)
                i *= i
        #print factor
        return sum(factor) == num
