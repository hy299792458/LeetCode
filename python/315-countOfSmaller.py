class Solution(object):
    def countSmaller(self, nums):
        def merge(nums):
            if len(nums) < 2:
                return nums
            else:
                mid = len(nums) / 2
                left = merge(nums[:mid])
                right = merge(nums[mid:])
            res = []
            cnt = l = r = 0
            for _ in range(len(nums)):
                if l < len(left) and (r == len(right) or left[l][1] <= right[r][1]):
                    self.smaller[left[l][0]] += cnt
                    res.append(left[l])
                    l += 1
                else:
                    cnt += 1
                    res.append(right[r])
                    r += 1
            return res
        self.smaller = [0 for _ in nums]
        merge(list(enumerate(nums)))
        return self.smaller
