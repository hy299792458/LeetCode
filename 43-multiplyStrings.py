class Solution(object):
    def multiply(self, num1, num2):
        pos = [0 for _ in range(len(num1) + len(num2))]
        for i in range(len(num1)):
            for j in range(len(num2)):
                temp = int(num1[- i - 1]) * int(num2[- j -1]) +  pos[i + j]
                pos[i + j] = temp % 10
                pos[i + j + 1] += temp /10
        r = len(pos) - 1
        while r >= 0 and pos[r] == 0:
            r -= 1
        return ''.join(map(str, pos[r::-1])) if r >= 0 else '0'
