class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        ugly = []
        bias = [-1 for _ in primes]
        temp = [1 for _ in primes]
        for _ in range(n):
            ugly.append(min(temp))
            for i in range(len(primes)):
                if temp[i] == ugly[-1]:
                    bias[i] += 1
                    temp[i] = primes[i] * ugly[bias[i]]
        return ugly[-1]
