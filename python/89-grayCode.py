class Solution(object):
    def grayCode(self, n):
        code = [0]
        total = 1
        for _ in range(n):
            temp = []
            for num in code[::-1]:
                temp.append(total + num)
            total *= 2
            code += temp
        return code
