class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        r = len(board[0])

        for i in range(n):
            h1 = {}
            for j in range(n):
                if board[i][j] != '.':
                    if board[i][j] in h1:
                        return False
                    else:
                        h1[board[i][j]] = 1

        for j in range(r):
            h2 = {}
            for i in range(r):
                if board[i][j] != '.':
                    if board[i][j] in h2:
                        return False
                    else:
                        h2[board[i][j]] = 1

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                h3 = {}
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        if board[k][l] != '.':
                            if board[k][l] in h3:
                                return False
                            else:
                                h3[board[k][l]] = 1

        return True