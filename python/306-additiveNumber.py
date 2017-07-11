class Solution(object):
    def isAdditiveNumber(self, num):
        l = len(num)
        for i in range(1, l):
            for j in range(i + 1, l):
                p = j
                num1 = num[:i]
                num2 = num[i:j]
                if str(int(num1)) != num1 or str(int(num2)) != num2:
                    continue
                while p < l:
                    num3 = str(int(num1) + int(num2))
                    if num[p:p+len(num3)] == num3:
                        num1, num2 = num2, num3
                        p += len(num3)
                    else:
                        p = l + 1
                if p == l:
                    return True
        return False
