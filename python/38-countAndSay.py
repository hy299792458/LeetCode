class Solution(object):
    def countAndSay(self, n):
        res = [1]
        for _ in range(n - 1):
            temp = res[0]
            count = 1
            newRes = []
            for num in res[1:] + [None]:
                if num == temp:
                    count += 1
                else:
                    newRes.append(count)
                    newRes.append(temp)
                    temp = num
                    count = 1
            res = newRes[:]
        return ''.join(map(str, res)) 
