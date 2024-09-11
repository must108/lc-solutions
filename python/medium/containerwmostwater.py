class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        res = []

        i = 0
        j = n-1

        while i < j:
            mi = min(height[i], height[j])
            res.append(mi * (j-i))
            if mi == height[i]:
                i += 1
            elif mi == height[j]:
                j -= 1

        return max(res)
