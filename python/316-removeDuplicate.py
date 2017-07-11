class Solution(object):
    def removeDuplicateLetters(self, s):
        pos = dict((c, p) for p, c in enumerate(s))
        stack = []
        used = set()
        for i in range(len(s)):
            char = s[i]
            if char not in used:
                while stack and char < stack[-1] and pos[stack[-1]] > i:
                    used.remove(stack.pop())
                used.add(char)
                stack.append(char)
        return ''.join(stack)
