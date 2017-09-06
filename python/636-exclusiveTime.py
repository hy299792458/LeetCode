class Solution(object):
    def exclusiveTime(self, n, logs):
        res = [0 for _ in range(n)]
        stack = []
        for l in logs:
            id, sta, t = l.split(':')
            if sta == 'end':
                red = 0
                while type(stack[-1]) == int:
                    red += stack.pop()
                id, s = stack.pop()
                time = int(t) - int(s) + 1 - red
                res[int(id)] += time
                stack.append(time + red)
            else:
                stack.append([id, t])
        return res
