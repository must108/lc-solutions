class Solution:
    def search(self, board: List[List[str]], word: str, row: int, col: int, index: int, m: int, n: int):
        if index == len(word) :
            return True
        elif(row < 0 or col < 0 or row == m or col == n or board[row][col] != word[index] or 
        board[row][col] == ''):  
            return False

        c = board[row][col]
        board[row][col] = ' '

        up = self.search(board, word, row - 1, col, index + 1, m, n)
        right = self.search(board, word, row, col + 1, index + 1, m, n)
        down = self.search(board, word, row + 1, col, index + 1, m, n)
        left = self.search(board, word, row, col - 1, index + 1, m, n)

        board[row][col] = c

        return up or right or down or left 

    def exist(self, board: List[List[str]], word: str):
        m = len(board)
        n = len(board[0])
        index = 0

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[index]:
                    if self.search(board, word, i, j, index, m, n):
                        return True

        return False
        