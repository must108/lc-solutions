class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = set(nums)

        res = 0
        for k in h:
            if k-1 not in h:
                l = 0
                while k+l in h:
                    l += 1
                res = max(l, res)
        return res