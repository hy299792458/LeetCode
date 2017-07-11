class Solution(object):
    def generate(self, numRows):
        if numRows <= 0:
            return []
        re = [[1]]
        for _ in range(1, numRows):
            temp = re[-1]
            line = [a + b for a, b in zip(temp, temp[1:])]
            re.append([1] + line + [1])
        return re
