class Solution(object):
    def canJump(self, nums):
        l = 0
        r = 1
        while True:
            if r >= len(nums):
                return True
            jump = 0
            for i in range(l, r):
                jump = max(jump, i + 1 + nums[i])
            if jump <= r:
                return False
            else:
                l = r
                r = jump
