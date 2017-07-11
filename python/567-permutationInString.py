class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        mapping = dict((w, p) for p, w in enumerate(set(s1)))
        target = [0 for _ in mapping]
        for char in s1:
            target[mapping[char]] += 1
        l = 0
        temp = [0 for _ in mapping]
        for r in range(len(s1)):
            if s2[r] in mapping:
                temp[mapping[s2[r]]] += 1
        if temp == target:
            return True
        r += 1
        while r < len(s2):
            if s2[l] in mapping:
                temp[mapping[s2[l]]] -= 1
            if s2[r] in mapping:
                temp[mapping[s2[r]]] += 1
            if temp == target:
                return True
            l += 1
            r += 1
        return False
