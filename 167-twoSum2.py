class Solution(object):
    def twoSum(self, numbers, target):
        seen = {}
        for i in range(len(numbers)):
            num = numbers[i]
            if target - num in seen:
                return seen[target-num] + 1, i + 1
            else:
                seen[num] = i
        
