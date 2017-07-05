class Solution(object):
    def hIndex(self, citations):
        citations.sort(reverse = True)
        i = 0
        while i < len(citations):
            if citations[i] >= i + 1:
                i += 1
            else:
                return i
        return len(citations)
