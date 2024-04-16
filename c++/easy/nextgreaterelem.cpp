#include <iostream>

class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stack;
        map<int, int> mp;
        vector<int> ret(nums1.size(), -1);

        for(int i = 0; i < nums2.size(); i++) {
            while(!stack.empty() && stack.top() < nums2[i]) {
                mp[stack.top()] = nums2[i];
                stack.pop();
            }
            stack.push(nums2[i]);
        }

        for(int i = 0; i < nums1.size(); i++) {
            if(mp[nums1[i]]) {
                ret[i] = mp[nums1[i]];
            }
        }

        return ret;
    }
};