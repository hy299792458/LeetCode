class Solution(object):
    def hammingDistance(self, x, y):
        binary = bin(x^y)
        #print binary
        return sum(1 for num in binary[2:] if num == '1')
