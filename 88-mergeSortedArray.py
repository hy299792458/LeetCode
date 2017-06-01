class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        re = []
        i = j = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                re.append(nums1[i])
                i += 1
            else:
                re .append(nums2[j])
                j += 1
        re += nums1[i:m]
        re += nums2[j:n]
        nums1[:m + n] = re[:]
