class Solution(object):
    def minWindow(self, s, t):
        mapping = dict((a, b) for b, a in enumerate(set(t)))
        length = len(set(t))
        count = [0 for _ in range(length)]
        for char in t:
            count[mapping[char]] += 1
        l = r = 0
        res = ''
        while r < len(s):
            try:
                while any(num > 0 for num in count):
                    if s[r] in mapping:
                        count[mapping[s[r]]] -= 1
                    r += 1
                while all(num <= 0 for num in count) and l < r:
                    if s[l] in mapping:
                        count[mapping[s[l]]] += 1
                    l += 1
                temp = s[l-1: r]
                if not res or len(res) > len(temp):
                    res = temp
            except:
                return res
        return res
