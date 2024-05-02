class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        h = []

        for n in nums:
            if n < 0:
                h.append(n)
        h.sort()

        for i in range(len(h)):
            if abs(h[i]) in nums:
                return abs(h[i])

        return -1