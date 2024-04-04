#include <iostream>

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> map1;
        int n = s.length();
        int left = 0, right = 0, maxLen = 0;

        for(right = 0; right < n; right++) {
            if(map1.count(s[right]) == 0 || map1[s[right]] < left) {
                map1[s[right]] = right;
                maxLen = max(maxLen, right - left + 1);
            } else {
                left = map1[s[right]] + 1;
                map1[s[right]] = right;
            }
        }

        return maxLen;
    }
};