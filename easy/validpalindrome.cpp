#include <iostream>

class Solution {
public:
    bool isPalindrome(string s) {
        vector<char> palin1;
        vector<char> palin2;

        for(int i = 0; i < s.length(); i++) {
            if(isalnum(s[i])) {
                palin1.push_back(tolower(s[i]));
            }
        }

        for(int i = palin1.size() - 1; i >= 0; i--) {
            palin2.push_back(palin1[i]);
        }

        return palin1 == palin2;
    }
};