class Solution(object):
    def decodeString(self, s):
        stack = []
        for char in s:
            if char == ']':
                string = []
                while stack[-1] != '[':
                    string.append(stack.pop())
                stack.pop()
                count = []
                while stack and stack[-1].isdigit():
                    count.append(stack.pop())
                stack.append(int(''.join(count[::-1])) * ''.join(string[::-1]))
            else:
                stack.append(char)
        return ''.join(stack)
