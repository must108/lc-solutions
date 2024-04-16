#include <iostream>

class Solution {
public:
    int romanToInt(string s) {
        int ret = 0;
        unordered_map<char, int> m1;
        m1['I'] = 1, m1['V'] = 5, m1['X'] = 10, m1['L'] = 50, m1['C'] = 100, m1['D'] = 500, m1['M'] = 1000;

        for(int i = 0; i < s.length(); i++) {
            if(m1[s[i]] < m1[s[i + 1]]) {
                ret -= m1[s[i]];
            } else {
                ret += m1[s[i]];
            }
        }

        return ret;
    }
};