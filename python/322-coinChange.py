class Solution(object):
    def coinChange(self, coins, amount):
        visited = set()
        temp = set([0])
        cnt = 0
        while temp:
            if amount in temp:
                return cnt
            cnt += 1
            newTemp = set()
            for val in temp:
                for c in coins:
                    if c + val not in visited and c + val <= amount:
                        newTemp.add(c + val)
                        visited.add(c + val)
            temp = newTemp
        return -1
