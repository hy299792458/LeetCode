class Solution(object):
    def intersect(self, nums1, nums2):
        dict1 = {}
        dict2 = {}
        for num in nums1:
            dict1[num] = dict1.get(num, 0) + 1
        for num in nums2:
            dict2[num] = dict2.get(num, 0) + 1
        re = []
        for k in dict1:
            re += [k] * min(dict1[k], dict2.get(k, 0))
        return re
