class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        n = len(heights)
        c = 0
        e = heights.copy()
        e.sort()

        for i in range(n):
            if heights[i] != e[i]:
                c += 1

        return c
