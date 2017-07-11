class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        re = set()
        for num in nums2:
            if num in seen:
                re.add(num)
        return list(re)
