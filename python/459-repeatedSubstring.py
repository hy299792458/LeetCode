class Solution(object):
    def repeatedSubstringPattern(self, s):
        for i in range(len(s) / 2):
            l = i + 1
            p = l
            pattern = s[:l]
            #print pattern
            while s[p : p + l] == pattern:
                p += l
            if p == len(s):
                return True
        return False

#use find() and extra space
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return (s*2)[1:-1].find(s) != -1
