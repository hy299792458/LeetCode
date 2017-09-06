class Solution(object):
    def find132pattern(self, nums):
        if len(set(nums)) < 3:
            return False
        stack = [[nums[0], nums[0]]]
        current_min = nums[0]
        for i in range(1, len(nums)):
            curr = nums[i]
            if curr >= stack[0][1]:  # curr >= max(nums[:i])
                stack = [[current_min, curr]]
            elif curr < current_min:  # curr < min(nums[:i])
                stack.append([curr, curr])
                current_min = curr
            elif curr == current_min:
                continue
            else:
                while stack and curr > stack[-1][0]:
                    if curr < stack[-1][1]:
                        return True
                    else:
                        stack.pop()
                stack.append([current_min, curr])
        return False
