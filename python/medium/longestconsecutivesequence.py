class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)
        res = 0
        
        for num in nums:
            if num - 1 not in h:
                l = 0
                while num + l in h:
                    l += 1
                res = max(l, res)
        return res