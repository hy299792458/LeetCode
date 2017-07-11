class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas):
            return -1
        minimal = [float('inf'), 0]
        temp = 0
        res = 0
        for i in range(len(gas)):
            bal = gas[i] - cost[i]
            temp += bal
            if temp < 0:
                temp = 0
                res = i + 1
        return res % len(gas)
