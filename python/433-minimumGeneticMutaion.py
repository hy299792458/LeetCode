class Solution(object):
    def minMutation(self, start, end, bank):
        if end not in bank:
            return -1
        bank = [start] + bank + [end]
        l = len(bank)
        adj = [[] for _ in range(l)]
        def check(s1, s2):
            count = 0
            for a, b in zip(s1, s2):
                if a != b:
                    count += 1
            return count == 1
        for i in range(l):
            for j in range(i + 1, l):
                if check(bank[i], bank[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        seen = set([0])
        temp = [0]
        count = 0
        while temp:
            newTemp = []
            for head in temp:
                for tail in adj[head]:
                    if tail not in seen:
                        seen.add(tail)
                        newTemp.append(tail)
            count += 1
            if l - 1 in seen:
                return count
            temp = newTemp
        return -1
