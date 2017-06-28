class Solution(object):
    def addStrings(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]
        res = []
        p1 = p2 = 0
        carry = 0
        while p1 < len(num1) and p2 < len(num2):
            n1 = int(num1[p1])
            n2 = int(num2[p2])
            temp = n1 + n2 + carry
            res.append(str(temp % 10))
            carry = temp / 10
            p1 += 1
            p2 += 1
        while p1 < len(num1):
            n1 = int(num1[p1])
            temp = n1 + carry
            res.append(str(temp % 10))
            carry = temp / 10
            p1 += 1
        while p2 < len(num2):
            n2 = int(num2[p2])
            temp = n2 + carry
            res.append(str(temp % 10))
            carry = temp / 10
            p2 += 1
        if carry:
            res.append(str(carry))
        return ''.join(res[::-1])
