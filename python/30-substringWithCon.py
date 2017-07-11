class Solution(object):
    def findSubstring(self, s, words):
        if not words:
            return []
        wordLen = len(words[0])
        matchLen = len(words)
        mapping = dict((w, p) for p, w in enumerate(set(words)))
        target = [0 for _ in range(len(mapping))]
        for word in words:
            target[mapping[word]] += 1
        res = []
        nums = map(lambda x: mapping.get(s[x: x+wordLen], -1), range(len(s)))
        for i in range(wordLen):
            try:
                l = i
                r = i
                temp = [0 for _ in target]
                while r < matchLen * wordLen + l:
                    if nums[r] != -1:
                        temp[nums[r]] += 1
                    r += wordLen
                if temp == target:
                    res.append(l)
                while r < len(s):
                    if nums[l] != -1:
                        temp[nums[l]] -= 1
                    if nums[r] != -1:
                        temp[nums[r]] += 1
                    l += wordLen
                    r += wordLen
                    if temp == target:
                        res.append(l)
            except:
                pass
        return res
