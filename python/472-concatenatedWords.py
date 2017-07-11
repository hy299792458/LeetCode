class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        words = set(words)
        def check(word):
            if word in words:
                return True
            for i in range(1, len(word)):
                if word[:i] in words and check(word[i:]):
                    return True
            return False
        res = []
        for word in words:
            words.remove(word)
            if check(word):
                res.append(word)
            words.add(word)
        return res 
