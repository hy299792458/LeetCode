class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        i = 0
        length = min([len(string) for string in strs])
        while i < length:
            common = strs[0][i]
            for string in strs[1:]:
                if common != string[i]:
                    return string[:i]
            i += 1
        return strs[0][:i]
