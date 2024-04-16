#include <iostream>

class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {   
        stack<int> stack;
        vector<int> temp(matrix[0].size(), 0);
        int area = 0;

        for(int i = 0; i < matrix.size(); i++) {
            for(int j = 0; j < matrix[i].size(); j++) {
                if(matrix[i][j] == '1') {
                    temp[j] += 1; 
                } else {
                    temp[j] = 0;
                }
            }

            int m = temp.size();
            for(int k = 0; k < m; k++) {
                while(!stack.empty() && temp[stack.top()] > temp[k]) {
                    int h = temp[stack.top()];
                    stack.pop();
                    int w = stack.empty() ? k : k - stack.top() - 1;
                    area = max(area, w * h);
                }
                stack.push(k);
            }

            while(!stack.empty()) {
                int h = temp[stack.top()];
                stack.pop();
                int w = stack.empty() ? m : m - stack.top() - 1;
                area = max(area, w * h);
            }
        }

        return area;
    }
};