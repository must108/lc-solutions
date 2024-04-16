#include <iostream>

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string str = "";
        int count = 0;

        while(count < word1.length() || count < word2.length()) {
            if(count < word1.length()) {
                str += word1[count];
            } 
            
            if(count < word2.length()) {
                str += word2[count];
            }

            count += 1;
        }

        return str;
    }
};