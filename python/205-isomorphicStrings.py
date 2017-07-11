class Solution(object):
    def isIsomorphic(self, s, t):
        pos1 = collections.defaultdict(list)
        pos2 = collections.defaultdict(list)
        for i in range(len(s)):
            pos1[s[i]].append(i)
        for j in range(len(t)):
            pos2[t[j]].append(j)
        v1 = pos1.values()
        v2 = pos2.values()
        v1.sort()
        v2.sort()
        return v1 == v2
