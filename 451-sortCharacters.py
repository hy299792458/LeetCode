class Solution(object):
    def frequencySort(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        string = list(char for char in set(s))
        string.sort(key = lambda x : -count[x])
        re = []
        for char in string:
            re += [char] * count[char]
        return ''.join(re)
