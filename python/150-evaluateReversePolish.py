class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for char in tokens:
            if char in ('+-*/'):
                num1 = stack.pop()
                num2 = stack.pop()
                if char == '+':
                    num = int(num1) + int(num2)
                elif char == '-':
                    num = int(num2) - int(num1)
                elif char == '/':
                    num = (abs(int(num2)) / abs(int (num1)))
                    num *= -1 if int(num1) * int(num2) < 0 else 1
                elif char == '*':
                    num = int(num1) * int(num2)
            else:
                num = int(char)
            stack.append(num)
            #print stack
        return int(stack[0])
