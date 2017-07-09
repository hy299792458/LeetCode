class Solution(object):
    def palindromePairs(self, words):
        wordDict = dict((w, p) for p, w in enumerate(words))
        res  = set()
        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                left = words[i][:j]
                right = words[i][j:]
                if left[::-1] in wordDict and right == right[::-1]:
                    res.add((i, wordDict[left[::-1]]))
                if right[::-1] in wordDict and left == left[::-1]:
                    res.add((wordDict[right[::-1]], i))
        return filter(lambda x: x[0] != x[1], list(res))
