class Solution(object):
    def calculate(self, s):
        s = s.replace(' ','')
        def cal(line):
            line = line.replace('--', '+')
            res = 0
            sig = 1
            num = '0'
            for char in line:
                if char in '+-':
                    res += int(num) * sig
                    num = '0'
                    sig = 1 if char == '+' else -1
                else:
                    num += char
            res += sig * int(num)
            #print line, res
            return res
        
        stack = []
        for char in s:
            if char == ')':
                line = []
                while stack[-1] != '(':
                    line.append(stack.pop())
                stack.pop()
                stack.append(str(cal(''.join(line[::-1]))))
            else:
                stack.append(char)
        return cal(''.join(stack))
