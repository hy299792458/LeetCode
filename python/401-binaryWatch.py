class Solution(object):
    def readBinaryWatch(self, num):
        hour = {}
        minute = {}
        for i in range(12):
            count = 0
            temp = i
            while temp:
                count += temp % 2
                temp /= 2
            hour[count] = hour.get(count, []) + [i]
            minute[count] = minute.get(count, []) + [i]
        for i in range(12, 60):
            count = 0
            temp = i
            while temp:
                count += temp % 2
                temp /= 2
            minute[count] = minute.get(count, []) + [i]
        
        res = []
        for l in range(num + 1):
            r = num - l
            res += [str(left) + ":" + '0' * (right < 10) + \
            str(right) for left in hour.get(l, []) for right \
            in minute.get(r, [])]
        return res
