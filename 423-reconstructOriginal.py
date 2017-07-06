class Solution(object):
    def originalDigits(self, s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        res = {}
        res['0'] = count.get('z', 0)
        res['6'] = count.get('x', 0)
        res['8'] = count.get('g', 0)
        res['2'] = count.get('w', 0)
        res['7'] = count.get('s', 0) - res['6']
        res['5'] = count.get('v', 0) - res['7']
        res['4'] = count.get('u', 0)
        res['1'] = count.get('o', 0) - res['2'] - res['4'] - res['0']
        res['3'] = count.get('h', 0) - res['8']
        res['9'] = count.get('i', 0) - res['8'] - res['5'] - res['6']
        line = []
        for k in sorted(res.keys()):
            line.append(k * res[k])
        return ''.join(line)
