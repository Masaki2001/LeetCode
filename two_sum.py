class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            tmp = target - nums[i]
            if tmp in d.keys():
                return [i, d[tmp]]
            d[nums[i]] = i

        return []

