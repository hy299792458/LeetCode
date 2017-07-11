class Solution(object):
    def divide(self, dividend, divisor):
        div = []
        sig = (dividend * divisor) >= 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while divisor <= dividend:
            div.append(divisor)
            divisor += divisor
        re = 0
        for num in div[::-1]:
            re *= 2
            if dividend >= num:
                re += 1
                dividend -= num
        if sig:
            return min(re, 2147483647)
        else:
            return max(-re, -2147483648)
