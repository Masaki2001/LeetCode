class Solution:
    def rob(self, nums: List[int]) -> int:
        now, past = 0, 0

        for n in nums:
            now, past = max(now, n + past), now

        return now