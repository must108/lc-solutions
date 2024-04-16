#include <iostream>

class Solution {
public:
    int lengthOfLastWord(string s) {
        int len = 0;
        int size = s.length() - 1;

        for(int i = size; i >= 0; i--) {
            if(s[i] == ' ') {
                size -= 1;
            } else {
                break;
            }
        }

        for(int i = size; i >= 0; i--) {
            if(s[i] != ' ') {
                len += 1;
            } else {
                break;
            }
        }

        return len;
    }
};