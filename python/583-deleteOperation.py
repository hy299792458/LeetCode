class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1 = len(word1) + 1
        l2 = len(word2) + 1
        store = [[None for _ in range(l1)] for _ in range(l2)]
        for i in range(l1):
            store[0][i] = i
        for j in range(l2):
            store[j][0] = j
        for i in range(1, l1):
            for j in range(1, l2):
                if word1[i-1] == word2[j - 1]:
                    temp = store[j-1][i-1] - 1
                    store[j][i] = min(store[j-1][i], store[j][i-1], temp) + 1
                else:
                    store[j][i] = min(store[j-1][i], store[j][i-1]) + 1
        return store[-1][-1]
