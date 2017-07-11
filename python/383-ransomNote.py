class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count = {}
        for w in magazine:
            count[w] = count.get(w, 0) + 1
        for w in ransomNote:
            count[w] = count.get(w, 0) - 1
        return all(x >= 0 for x in count.values())
