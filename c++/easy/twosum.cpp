#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ret = {};

        for(int i = 0; i < nums.size(); i++) {
            for(int j = 1; j < nums.size(); j++) {
                if(i == j){
                    continue;
                }

                if(nums[i] + nums[j] == target) {
                    ret = {i, j};
                    return ret;
                }
            }
        }
        return ret;
    }
};