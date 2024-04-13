#include <iostream>

class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        stack<int> stack;
        int area = 0;

        for(int i = 0; i < n; i++) {
            while(!stack.empty() && heights[stack.top()] > heights[i]) {
                int h = heights[stack.top()];
                stack.pop();
                int w = stack.empty() ? i : i - stack.top() - 1;
                area = max(area, w * h);
            } 
            stack.push(i);
        }

        while(!stack.empty()) {
            int h = heights[stack.top()];
            stack.pop();
            int w = stack.empty() ? n : n - stack.top() - 1;
            area = max(area, w * h);
        }

        return area;
    }
};