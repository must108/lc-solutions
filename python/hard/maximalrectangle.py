class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        temp = [0] * (cols + 1)
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == '1':
                    temp[j] += 1
                else:
                    temp[j] = 0

            stk = []
            for k in range(len(temp)):
                while stk and temp[stk[-1]] > temp[k]:
                    h = temp[stk.pop()]
                    w = k if not stk else k - stk[-1] - 1
                    max_area = max(max_area, h * w)
                stk.append(k)

        return max_area
