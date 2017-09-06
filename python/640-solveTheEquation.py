class Solution(object):
    def solveEquation(self, equation):
        def simplify(line):
            line += '+'
            res = [0, 0]
            temp = ''
            sig = 1
            for char in line:
                if char in '+-':
                    if temp:
                        if temp[-1] == 'x':
                            if temp == 'x':
                                res[0] += sig
                            else:
                                res[0] += int(temp[:-1])* sig
                        else:
                            res[1] += int(temp) * sig
                    temp = ''
                    sig = 1 if char == '+' else -1
                else:
                    temp += char
            return res
        lr = equation.split('=')
        l = simplify(lr[0])
        r = simplify(lr[1])
        print l, r
        if l[0] == r[0]:
            if r[1] == l[1]:
                return "Infinite solutions"
            else:
                return "No solution"
        return "x=" + str((r[1] - l[1])  / (l[0] - r[0]))
