#include <iostream>

class Solution {
public:
    bool isPerfectSquare(int num) {
        int left = 0, right = num;
        while(left <= right) {
            long long int mid = (left + right) / 2;
            if(mid * mid == num) {
                return true;
            } else if(mid * mid > num) {
                right = mid - 1;
            } else if(mid * mid < num) {
                left = mid + 1;
            } else {
                return false;
            }
        }
        return false;
    }
};