#include <iostream>

class Solution {
public:
    string makeGood(string s) {
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == s[i + 1] - 32 || s[i] == s[i + 1] + 32) {
                s.erase(s.begin() + i);
                s.erase(s.begin() + i);
                i = -1;
            }
        }

        return s;
    }
};