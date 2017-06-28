class Solution(object):
    def nearestPalindromic(self, n):
        cand = []
        nums = list(n)
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] != nums[r]:
                nums[r] = nums[l]
            r -= 1
            l += 1
        cand.append(''.join(nums))
        if len(nums) > 1:
            cand.append('9' * (len(nums) - 1))
        cand.append('1' + '0' * (len(nums) - 1) + '1')
        if int(nums[l]) < 9:
            temp = nums[:]
            temp[l] = temp[r] = str(int(temp[l]) + 1)
            cand.append(''.join(temp))
        if int(nums[l]) > 0:
            temp = nums[:]
            temp[l] = temp[r] = str(int(temp[l]) - 1)
            cand.append(''.join(temp))
        cand = filter(lambda x: x!= n, cand)
        return min(cand, key = lambda x: (abs(int(x) - int(n)), int(x)))
