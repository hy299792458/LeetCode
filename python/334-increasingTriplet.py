class Solution(object):
    def increasingTriplet(self, nums):
        stack = []
        for num in nums:
            if not stack or num > stack[-1]:
                stack.append(num)
            elif num <= stack[0]:
                stack[0] = num
            elif len(stack) > 1 and stack[1] >= num:
                stack[1] = num
            if len(stack) == 3:
                return True
            #print stack
        return False
