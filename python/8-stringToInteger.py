class Solution(object):
    def myAtoi(self, string):
        string = string.lstrip()
        i = 0
        sig = 1
        res = 0
        if not string:
            return 0
        if string[i] in '+-':
            sig = -1 if string[i] == '-' else 1
            i += 1
        print string
        while i < len(string):
            if string[i].isdigit():
                res *= 10
                res += int(string[i])
            else:
                break
            i += 1
        res *= sig
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648
        return res
