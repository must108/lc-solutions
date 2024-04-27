class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)

        for r in range(1, n):
            for c in range(n):
                mid = grid[r - 1][c] 
                left = grid[r - 1][c - 1] if c > 0 else float("inf")
                right = grid[r - 1][c + 1] if c < n - 1 else float("inf")
                res = min(mid, left, right)
                grid[r][c] = grid[r][c] + min(grid[r-1][:c] + grid[r-1][c+1:])

        return min(grid[-1])
        