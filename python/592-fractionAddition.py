class Solution(object):
    def fractionAddition(self, expression):
        up = []
        down = []
        temp = expression[0]
        for char in expression[1:]:
            if char == '/':
                up.append(temp)
                temp = ''
            elif char in ['+', '-']:
                down.append(temp)
                temp = char
            else:
                temp += char
        down.append(temp)
        
        def add(a, b):
            u1, d1 = int(a[0]), int(a[1])
            u2, d2 = int(b[0]), int(b[1])
            u = u1 * d2 + u2 * d1
            d = d1 * d2
            n1, n2 = u, d
            while n1 % n2 != 0:
                n1, n2 = n2, n1 % n2
            return [u/n2, d/n2]
        upNum, downNum = reduce(add, [[up[i], down[i]] for i in range(len(up))])
        return str(upNum) + '/' + str(downNum)
        
        
