class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        for char in num:
            if not stack or stack[-1] <= char or k == 0:
                stack.append(char)
            else:
                while k > 0 and stack and stack[-1] > char:
                    stack.pop()
                    k -= 1
                stack.append(char)
        while k > 0:
            stack.pop()
            k -= 1
        return str(int(''.join(stack))) if stack else '0'
