#include <iostream>

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector<int> ret = {};
        int start = 0, end = numbers.size() - 1;

        while(start <= end) {
            if(numbers[start] + numbers[end] == target) {
                ret = {start + 1, end + 1};
                return ret;
            } else if(numbers[start] + numbers[end] > target) {
                end -= 1;
            } else if(numbers[start] + numbers[end] < target) {
                start += 1;
            }
        }

        return ret;
    }
};