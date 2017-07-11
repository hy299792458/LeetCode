class Solution(object):
    def firstUniqChar(self, s):
        pos = collections.defaultdict(list)
        for i in range(len(s)):
            pos[s[i]].append(i)
        re = float('inf')
        for l in pos.values():
            if len(l) == 1:
                re = min(re, l[0])
        return re if re < float('inf') else -1
