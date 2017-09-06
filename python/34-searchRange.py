class Solution(object):
    def searchRange(self, nums, target):
        result = [-1, -1]
        start = 0
        end = len(nums) - 1

        if len(nums) < 1 or nums[start] > target or nums[end] < target:
            return result

        while True:
            if start == end or start == end - 1:
                break
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        if nums[start] == target:
            result[0] = start
        elif nums[end] == target:
            result[0] = end
        start = 0
        end = len(nums) - 1
        while True:
            if start == end or start == end - 1:
                break
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid
        if nums[end] == target:
            result[1] = end
        elif nums[start] == target:
            result[1] = start
        return result
