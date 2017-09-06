class Solution(object):
    def maximumSwap(self, num):
        digs = [c for c in str(num)]
        for i in range(len(digs)):
            temp = max(digs[i :])
            if digs[i] < temp:
                for j in range(i + 1, len(digs)):
                    if digs[j] == temp:
                        p = j
                digs[p], digs[i] = digs[i], digs[p]
                return int(''.join(digs))
        return int(''.join(digs))
