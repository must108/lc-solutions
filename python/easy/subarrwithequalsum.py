class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        subs = 0
        n = len(nums)
        h = {}

        for i in range(n-1):
            if nums[i] + nums[i+1] in h:
                return True
            else:
                h[nums[i] + nums[i+1]] = 1

        return False