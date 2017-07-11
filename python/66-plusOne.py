class Solution(object):
    def plusOne(self, digits):
        carry = 1
        i = len(digits) - 1
        while i >= 0 and carry:
            temp = digits[i] + carry
            digits[i] = temp % 10
            carry = temp / 10
            i -= 1
        return [carry] + digits if carry else digits
