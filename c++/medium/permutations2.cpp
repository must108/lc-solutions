#include <iostream>

class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> ans;
        backtracking(nums, 0, nums.size() - 1, ans);
        return ans;
    }

    void backtracking(vector<int>& vect, int l, int r, vector<vector<int>>& retVect) {
        if(l == r && (find(retVect.begin(), retVect.end(), vect) == retVect.end())) {
            retVect.push_back(vect);
        } else {
            for(int i = l; i <= r; i++) {
                swap(vect[l], vect[i]);
                backtracking(vect, l + 1, r, retVect);
                swap(vect[i], vect[l]);
            }
        }
    }
};