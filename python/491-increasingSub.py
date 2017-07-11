class Solution(object):
    def findSubsequences(self, nums):
        re = [()]
        for num in nums:
            temp = []
            for l in re:
                if l == () or num >= l[-1]:
                    temp.append(tuple(list(l) + [num]))
            re += temp
        re =  list(set(re))
        return filter(lambda x: len(x) >= 2, re)
