class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(1, len(prices)):
            diff = max(prices[i] - prices[i - 1], 0)
            ans += diff

        return ans
