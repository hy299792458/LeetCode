class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sig = '-' if denominator * numerator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)
        div = numerator / denominator
        res = numerator % denominator
        nums = []
        seen = {}
        pos = 0
        while res and res not in seen:
            seen[res] = pos
            pos += 1
            res *= 10
            nums.append(res / denominator)
            res = res % denominator
        if not nums:
            return sig + str(div)
        if not res:
            return sig + str(div) + '.' + ''.join(map(str, nums))
        else:
            p = seen[res]
            return sig + str(div) + '.' + ''.join(map(str, nums[:p])) + '(' + ''.join(map(str, nums[p:])) + ')'
