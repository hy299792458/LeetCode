class Solution(object):
    def diffWaysToCompute(self, input):
        def operate(n1, n2, op):
            if op == '+':
                return int(n1) + int(n2)
            elif op == '-':
                return int(n1) - int(n2)
            else:
                return int(n1) * int(n2)
        temp = ''
        line = []
        for char in input:
            if char in '+-*':
                line.append(temp)
                temp = ''
                line.append(char)
            else:
                temp += char
        line.append(temp)
        
        dp = {}
        def divide(line):
            if line in dp:
                return dp[line]
            nums = line.split(',')
            l = len(nums)
            if l == 1:
                res = map(int, nums)
            elif l == 3:
                res = [operate(nums[0], nums[2], nums[1])]
            else:
                res = []
                for i in range(l / 2):
                    mid = 2 * i + 1
                    res += [operate(l1, l2, nums[mid]) for l1 in divide(','.join(nums[:mid])) for l2 in divide(','.join(nums[mid + 1:]))]
            dp[line] = res
            return res
        
        return divide(','.join(line))
