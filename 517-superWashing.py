class Solution(object):
    def findMinMoves(self, machines):
        num = len(machines)
        total = sum(machines)
        if total % num != 0:
            return -1
        mean = total / num
        unbal = 0
        res = 0
        for mac in machines:
            if mac > mean:
                res = max(res, abs(mac - mean), abs(unbal), abs(unbal + mac - mean))
            else:
                res = max(res, abs(unbal), abs(unbal + mac - mean))
            unbal += (mac - mean)
        return res
