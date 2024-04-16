#include <iostream>

class Solution {
public:
    string removeKdigits(string num, int k) {
        stack<char> stk;

        for(char digit : num) {
            while(!stk.empty() && stk.top() > digit && k > 0) {
                stk.pop();
                k -= 1;
            }
            stk.push(digit);
        }

        while(k > 0 && !stk.empty()) {
            stk.pop();
            k -= 1;
        }

        string temp = "";
        while(!stk.empty()) {
            temp.push_back(stk.top());
            stk.pop();
        }
        reverse(temp.begin(), temp.end());

        string res = "";
        int found = 0, m = temp.size();
        for(int i = 0; i < m; i++) {
            if(temp[i] == '0' && found == 0) {
                continue;
            } else {
                res.push_back(temp[i]);
                found = 1;
            }
        }

        if(res.size() == 0) {
            res.push_back('0');
        }

        return res;
    }
};