#include <iostream>

class Solution {
public:
    bool isPalindrome(int x) {
        string ret = std::to_string(x);
        vector<char> palin1;
        vector<char> palin2;

        for(int i = 0; i < ret.length(); i++) {
            palin1.push_back(ret[i]);
        }

        for(int i = palin1.size() - 1; i >= 0; i--) {
            palin2.push_back(palin1[i]);
        }

        return palin1 == palin2;
    }
};