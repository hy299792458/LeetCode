class Solution(object):
    def wordPattern(self, pattern, str):
        pos1 = collections.defaultdict(list)
        pos2 = collections.defaultdict(list)
        for i in range(len(pattern)):
            pos1[pattern[i]].append(i)
        words = str.split(' ')
        for j in range(len(words)):
            pos2[words[j]].append(j)
        v1 = pos1.values()
        v1.sort()
        v2 = pos2.values()
        v2.sort()
        return v1 == v2
