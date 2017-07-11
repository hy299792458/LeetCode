class Solution(object):
    def findRotateSteps(self, ring, key):
        pos = collections.defaultdict(list)
        for p, k in enumerate(ring):
            pos[k].append(p)
        temp = [[0, 0]]
        l = len(ring)
        def dist(a, b):
            return min(abs(a - b), l - abs(a - b))
        for k in key:
            newTemp = []
            for post in pos[k]:
                newTemp.append([post, min(c + dist(post, p) for p, c in temp)])
            temp = newTemp
        return min(c for p, c in temp) + len(key)
