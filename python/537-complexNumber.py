class Solution(object):
    def complexNumberMultiply(self, a, b):
        r1, i1 = a[:-1].split('+')
        r2, i2 = b[:-1].split('+')
        re = int(r1) * int(r2) - int(i1) * int(i2)
        im = int(r1) * int(i2) + int(r2) * int(i1)
        return str(re) + '+' + str(im) + 'i'
