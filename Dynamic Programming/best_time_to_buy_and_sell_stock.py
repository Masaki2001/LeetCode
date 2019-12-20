class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        ans = 0
        minNum = prices[0]

        for n in prices[1:]:
            ans, minNum = max(ans, n - minNum), min(n, minNum)

        return ans
