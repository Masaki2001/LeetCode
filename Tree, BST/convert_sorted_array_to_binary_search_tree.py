# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        center = len(nums) // 2
        leftCenter = nums[:center]
        rightCenter = nums[center + 1:]

        ans = TreeNode(nums[center])
        ans.left = self.sortedArrayToBST(leftCenter)
        ans.right = self.sortedArrayToBST(rightCenter)

        return ans

