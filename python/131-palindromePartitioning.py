class Solution(object):
    def partition(self, s):
        res = []
        def check(s):
            return s == s[::-1]
        def dfs(p, path):
            if p == len(s):
                res.append(path[:])
            else:
                for j in range(p + 1, len(s) + 1):
                    if check(s[p: j]):
                        dfs(j, path + [s[p:j]])
        dfs(0, [])
        return res