class Solution(object):
    def groupAnagrams(self, strs):
        res = collections.defaultdict(list)
        for string in strs:
            res[tuple(sorted(string))].append(string)
        return res.values()
