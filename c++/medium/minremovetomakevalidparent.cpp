#include <iostream>

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> sta1;

        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(') {
                sta1.push(i);
            } else if(s[i] == ')') {
                if(!sta1.empty()) {
                    sta1.pop();
                } else {
                    s[i] = '*';
                }
            }
        }

        while(!sta1.empty()) {
            s[sta1.top()] = '*';
            sta1.pop();
        }

        string result = "";
        for(char c : s) {
            if(c != '*') {
                result += c;
            }
        }

        return result;
    }
};