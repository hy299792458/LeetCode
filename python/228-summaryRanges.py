class Solution(object):
    def summaryRanges(self, nums):
        res = []
        if not nums:
            return []
        temp = nums[0]
        l = 1
        for num in nums[1:]:
            if num == temp + l:
                l += 1
            elif l == 1:
                res.append(str(temp))
                temp = num
            else:
                res.append(str(temp) + '->' + str(temp + l - 1))
                l = 1
                temp = num
        if l == 1:
            res.append(str(temp))
        else:
            res.append(str(temp) + '->' + str(temp + l - 1))
        return res
                
