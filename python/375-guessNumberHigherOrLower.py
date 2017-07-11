class Solution(object):
    def getMoneyAmount(self, n):
        cost = {}
        def dp(i,j):
            if (i, j) in cost:
                return cost[(i,j)]
            else:
                if i >= j :
                    co = 0
                else:
                    co = float('inf')
                    for mid in range(i, j):
                        temp = mid + max(dp(i, mid - 1), dp(mid + 1, j))
                        co = min(temp, co)
                cost[(i, j)] = co
                return co
        return dp(1, n)
                        
