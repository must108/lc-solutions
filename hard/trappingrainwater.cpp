#include <iostream>

class Solution {
public:
    int trap(vector<int>& height) {
        stack<int> stack;
        int ans = 0;

        for(int i = 0; i < height.size(); i++) {
            while(!stack.empty() && height[stack.top()] < height[i]) {
                int popHeight = height[stack.top()];
                stack.pop();

                if(stack.empty()) break;

                int dist = i - stack.top() - 1;
                int minHeight = min(height[stack.top()], height[i]) - popHeight;
                ans += dist * minHeight;
            }
            stack.push(i);
        }

        return ans;
    }
};