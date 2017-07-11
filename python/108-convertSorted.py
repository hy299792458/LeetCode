# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        def gen(l, r):
            if l >= r:
                return None
            mid = (l + r) / 2
            re = TreeNode(nums[mid])
            re.left = gen(l, mid)
            re.right = gen(mid + 1, r)
            return re
        return gen(0, len(nums))
