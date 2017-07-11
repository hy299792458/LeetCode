class Solution(object):
    def calculate(self, s):
        line = []
        temp = ''
        sign = '+'
        for char in s+'+':
            if char.isdigit():
                temp += char
            elif char != ' ':
                if sign == '+':
                    line.append(int(temp))
                elif sign == '-':
                    line.append(-int(temp))
                elif sign == '*':
                    line.append(line.pop() * int(temp))
                elif sign == '/':
                    num = line.pop()
                    line.append(num / int(temp) if num * int(temp) > 0 else -(-num / int(temp)) )
                temp = ''
                sign = char
        return sum(line)
