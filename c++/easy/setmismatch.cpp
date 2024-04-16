#include <iostream>

class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        set<int> s1;
        int size = nums.size();

        int arrSum = 0;
        int setSum = 0;
        int expSum = size * (size + 1) / 2;

        for(auto& num : nums) {
            s1.insert(num);
            arrSum += num;
        }

        for(auto& num : s1) {
            setSum += num;
        }

        int duplicate = arrSum - setSum;
        int mismatch = expSum - setSum;

        return {duplicate, mismatch};
    }
};