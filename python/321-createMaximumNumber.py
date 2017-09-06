class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m= len(nums1),len(nums2)
        ret = [0] * k
        for i in range(0, k+1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.mergeMax(left, right)
            ret = max(num, ret)
        return ret


    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0],
                nums1 = nums1[1:]
            else:
                ans += nums2[0],
                nums2 = nums2[1:]
        return ans

    def maxSingleNumber(self, nums, selects):
        n = len(nums)
        ret = [-1]
        if selects > n : return ret
        while selects > 0:
            start = ret[-1] + 1 #search start
            end = n-selects + 1 #search end
            ret.append( max(range(start, end), key = nums.__getitem__))
            selects -= 1
        ret = [nums[item] for item in ret[1:]]
        return ret
