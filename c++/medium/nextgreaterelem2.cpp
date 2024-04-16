#include <iostream>

class Solution {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();
        stack<int> stack;
        vector<int> ret(n, -1);

        for(int i = (2*n) - 1; i >= 0; i--) {
            while(!stack.empty() && stack.top() <= nums[i % n]) {
                stack.pop();
            }
            if(!stack.empty() && i < n) {
                ret[i] = stack.top();
            } 
            stack.push(nums[i % n]);
        }

        return ret;
    }
};