class Solution(object):
    store = {}
    def isScramble(self, s1, s2):
        #print s1, s2
        if (s1, s2) in self.store:
            return self.store[(s1, s2)]
        if s1 == s2:
            res =  True
        else:
            res = False
            for i in range(1, len(s1)):
                if sorted(s1[:i]) == sorted(s2[-i:]):
                    res |= self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])
                if sorted(s1[:i]) == sorted(s2[:i]):
                    res |= self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])
        self.store[(s1, s2)] = res
        return res
