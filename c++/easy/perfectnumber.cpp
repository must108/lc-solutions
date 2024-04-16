#include <iostream>

class Solution {
public:
    bool checkPerfectNumber(int num) {
        int *arr = new int[num];
        int count = 0;
        int temp = 0;
        for(int i = 1; i < num; i++) {
            if(num % i == 0) {
                arr[count] = i;
                count += 1;
            }
        }

        for(int i = 0; i < count; i++) {
            temp += arr[i];
        }

        if(temp == num) {
            return true;
        } else {
            return false;
        }
    }
};