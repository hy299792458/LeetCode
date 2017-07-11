class Solution(object):
    def reconstructQueue(self, people):
        pos = [i for i in range(len(people))]
        res = [0 for _ in people]
        people.sort()
        bias = {}
        for peo in people:
            #print pos, peo
            p = pos[peo[1] - bias.get(peo[0], 0)]
            bias[peo[0]] = bias.get(peo[0], 0) + 1
            res[p] = peo
            pos.remove(p)
        return res
