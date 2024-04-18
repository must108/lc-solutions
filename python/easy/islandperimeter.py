class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        peri = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    peri += 4
                    if i is not (n - 1):
                        if grid[i + 1][j] == 1:
                            peri -= 1
                    if i is not 0:
                        if grid[i - 1][j] == 1:
                            peri -= 1
                    if j is not (m - 1):
                        if grid[i][j + 1] == 1:
                            peri -= 1
                    if j is not 0:
                        if grid[i][j - 1] == 1:
                            peri -= 1

        return peri