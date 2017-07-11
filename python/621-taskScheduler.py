class Solution(object):
    def leastInterval(self, tasks, n):
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        maxcount = [0, 0]
        for num in count.values():
            if num > maxcount[0]:
                maxcount = [num, 1]
            elif num == maxcount[0]:
                maxcount[1] += 1
        re1 = len(tasks)
        re2 = (n + 1) * (maxcount[0] - 1) + maxcount[1]
        return max(re1, re2)
