class Solution(object):
    def findLUSlength(self, strs):
        strs.sort(key = len, reverse = True)
        def aInB(a, b):
            a = iter(a)
            return all(char in a for char in b)
        temp = [True for _ in strs]
        for i in range(len(strs)):
            if not any(aInB(strs[j], strs[i]) for j in range(i)):
                if strs[i] not in strs[i + 1:]:
                    return len(strs[i])
        return -1
