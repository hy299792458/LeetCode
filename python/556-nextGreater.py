class Solution(object):
    def nextGreaterElement(self, n):
        n = [char for char in str(n)]
        for i in xrange(len(n) - 1, 0, -1):
            if n[i] > n[i - 1]:
                left = n[: i - 1]
                right = n[i - 1:]
                temp = min(char for char in right if char > n[i - 1])
                right.remove(temp)
                right.sort()
                res = int(''.join(left + [temp] + right))
                return res if res < 2 ** 31 - 1 else -1
        return -1
