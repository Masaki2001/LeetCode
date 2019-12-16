class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ansArray = []
        fewArray = nums1 if len(nums1) < len(nums2) else nums2
        manyArray = nums1 if len(nums1) > len(nums2) else nums2
        for i, num in enumerate(fewArray):
            if num in manyArray and not num in ansArray:
                ansArray.append(num)
        return ansArray
