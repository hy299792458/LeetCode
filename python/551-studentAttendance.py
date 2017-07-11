class Solution(object):
    def checkRecord(self, s):
        A = 0
        for i in range(len(s)):
            if s[i] == 'A':
                if A != 0:
                    return False
                A += 1
            elif s[i] == 'L':
                if i > 1 and s[i - 1] == 'L' and s[i - 2] == 'L':
                    return False
        return True
