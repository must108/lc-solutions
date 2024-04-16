#include <iostream>

class Solution {
    bool search(vector<vector<char>> &board, string word, int row, int col, int index, int m, int n) {
        if(index == word.length()) {
            return true;
        } else if(row < 0 || col < 0 || row == m || col == n || board[row][col] != word[index] || board[row][col] == ' ') {
            return false;
        }

        char c = board[row][col];
        board[row][col] = ' ';

        bool up = search(board, word, row - 1, col, index + 1, m, n);
        bool right = search(board, word, row, col + 1, index + 1, m, n);
        bool down = search(board, word, row + 1, col, index + 1, m, n);
        bool left = search(board, word, row, col - 1, index + 1, m, n);

        board[row][col] = c;

        return up || right || down || left;
    }


public:
    bool exist(vector<vector<char>>& board, string word) {
        int m = board.size(), n = board[0].size();
        int index = 0;

        for(int i = 0; i < m; i++) {
            for(int j = 0; j < n; j++) {
                if(board[i][j] == word[index]) {
                    if(search(board, word, i, j, index, m, n)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
};