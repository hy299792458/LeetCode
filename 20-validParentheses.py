class Solution(object):
    def isValid(self, s):
        stack = []
        mapping = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in "({[":
                stack.append(char)
            else:
                if not stack or mapping[stack[-1]] != char:
                    return False
                stack.pop()
        return stack == []
                    
