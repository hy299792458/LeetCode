class Solution(object):
    def countBits(self, num):
        res = [0 for _ in range(num + 1)]
        mode = 1
        for i in range(1, (num + 1)):
            if i >= 2 * mode:
                mode *= 2
            res[i] = res[i - mode] + 1
        return res
