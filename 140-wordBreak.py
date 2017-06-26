class Solution(object):
    def wordBreak(self, s, wordDict):
        isWord = [[] for _ in range(len(s) + 1)]
        isWord[0] = 0
        for i in range(1, len(s) + 1):
            for j in range(i):
                if isWord[j] != [] and s[j:i] in wordDict:
                    isWord[i].append(j)
        print isWord
        self.result = []
        def DFS(end, temp):
            if end == 0:
                self.result.append(' '.join(temp[::-1]))
            else:
                for start in isWord[end]:
                    DFS(start, temp + [s[start: end]])
        DFS(len(s), [])
        return self.result

#elegent DP solution
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        memo = {}
        def helper(s):
            if s in memo: return memo[s]
            res = []
            if s in wordDict:
                res.append(s)
            for i in range(len(s)):
                cur = s[:i+1]
                if cur in wordDict:
                    temp = helper(s[i+1:])
                    for item in temp:
                        res.append(cur + " " + item)
            memo[s] = res
            return res 
        return helper(s)
