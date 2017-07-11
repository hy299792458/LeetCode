class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        stack = []
        pos = {}
        for num in nums:
            if not stack or stack[-1] > num:
                stack.append(num)
            else:
                while stack and stack[-1] < num:
                    pos[stack.pop(-1)] = num
                stack.append(num)
        return map(lambda x: pos.get(x, -1), findNums)
