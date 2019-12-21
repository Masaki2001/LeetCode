class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = cur = nums[0]

        for n in nums[1:]:
            cur = max(n, n + cur)
            ans = max(cur, ans)

        return ans
