class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        h = {}

        for num in nums:
            h[num] = 1 + h.get(num, 0)

        return sorted(nums, key=lambda num: (h[num], -num))            