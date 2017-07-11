class Solution(object):
    def nthUglyNumber(self, n):
        primes = [2, 3, 5]
        index = [-1] * 3
        temp = [1] * 3
        ugly = []
        for _ in range(n):
            ugly.append(min(temp))
            for i in range(3):
                if temp[i] == ugly[-1]:
                    index[i] += 1
                    temp[i] = ugly[index[i]] * primes[i]
        return ugly[-1]
