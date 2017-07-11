class Solution(object):
    def generateParenthesis(self, n):
        re = []
        def add(l, r, temp):
            if l == r == 0:
                re.append(temp)
            if l < r:
                add(l, r - 1, temp + ')')
            if l > 0:
                add(l - 1, r, temp + '(')
        add(n, n, '')
        return re
