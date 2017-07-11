class Solution(object):
    def hIndex(self, citations):
        l = 0
        r = len(citations)
        while True:
            if r <= l:
                return len(citations) - l
            mid = (l + r) / 2
            if citations[mid] >= len(citations) - mid:
                r = mid
            else:
                l = mid + 1
