#include <iostream>

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        int n = temperatures.size();
        stack<int> stack;
        map<int, int> mp;
        vector<int> ret(n, 0);
        
        for(int i = 0; i < n; i++) {
            while(!stack.empty() && temperatures[stack.top()] < temperatures[i]) {
                ret[stack.top()] = i - stack.top();
                stack.pop();
            }
            stack.push(i);
        }
        return ret;
    }
};