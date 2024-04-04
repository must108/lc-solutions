#include <iostream>

class Solution {
public:
    int maxDepth(string s) {
        int counter = 0, maximum = 0;

        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(') {
                counter += 1;
                maximum = max(maximum, counter);
            } else if(s[i] == ')') {
                counter -= 1;
                maximum = max(maximum, counter);
            }
        }
        return maximum;
    }
};