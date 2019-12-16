# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    count = 0

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return sum is 0 and self.count > 0

        self.count += 1
        result = 0

        diff = sum - root.val

        if diff is 0 and root.left is None and root.right is None:
            return True

        if root.left is not None:
            result = result or self.hasPathSum(root.left, diff)

        if root.right is not None:
            result = result or self.hasPathSum(root.right, diff)

        return result