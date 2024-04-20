class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n, m = len(land), len(land[0])
        res = []

        def dfs(r, c):
            if r < 0 or c < 0 or r == n or c == m or land[r][c] == 0:
                return [0, 0]
            
            land[r][c] = 0
            down = dfs(r+1, c)
            right = dfs(r, c+1)

            return [max(r, down[0], right[0]), max(c, down[1], right[1])]

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    arr = dfs(i, j)
                    res.append([i, j, arr[0], arr[1]])

        return res