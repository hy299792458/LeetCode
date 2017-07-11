class Solution(object):
    def isPowerOfFour(self, num):
	#solution 1, much slower
        if num <= 0:
            return False
        num = bin(num)
        order = [i for i in range(1, len(num) - 1) if num[-i] == '1']
        return len(order) == 1 and order[0] % 2 == 1

    def isPowerOfFour(self, num):
        return num != 0 and num &(num-1) == 0 and num & 1431655765== num
