class Solution(object):
    def combinationSum3(self, k, n):
        self.res = []
        def dfs(num, temp, k):
            if k == 0 and sum(temp) == n:
                self.res.append(temp)
            elif k > 0:
                for i in range(num + 1, 10):
                    if sum(temp) + num > n:
                        break
                    dfs(i, temp + [i], k - 1)
        dfs(0, [], k)
        return self.res
