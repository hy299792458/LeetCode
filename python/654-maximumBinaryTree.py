# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if not nums:
            return None
        find = max(zip(nums, range(len(nums))))
        root = TreeNode(find[0])
        root.left = self.constructMaximumBinaryTree(nums[: find[1]])
        root.right = self.constructMaximumBinaryTree(nums[find[1] + 1:])
        return root
