class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #         以下、失敗
        #         count = 0
        #         for i, n in enumerate(nums):
        #             if n == 0:
        #                 del nums[i]
        #                 count += 1

        #         for c in range(count):
        #             nums.append(0)

        count = 0
        while 0 in nums:
            nums.remove(0)
            count += 1

        for c in range(count):
            nums.append(0)