class Solution(object):
    def isPossible(self, nums):
        cnt = dict()
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        for num in set(nums):
            a = cnt.get(num - 2, 0)
            b = cnt.get(num - 1, 0)
            c = cnt.get(num)
            d = cnt.get(num + 1, 0)
            e = cnt.get(num + 2, 0)
            l = min(a, b)
            r = min(d, e)
            a -= l
            b -= l
            c -= (l + r)
            d -= r
            e -= r
            if c > 0 and c > min(b, d):
                return False
