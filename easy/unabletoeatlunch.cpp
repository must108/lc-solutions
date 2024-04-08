#include <iostream>

class Solution {
public:
    int countStudents(vector<int>& students, vector<int>& sandwiches) {
        queue<int> q;
        int count = 0;

        for(auto i : students) {
            q.push(i);
        }

        int i = 0;
        while(q.size() > 0 && count != q.size()) {
            if(q.front() == sandwiches[i]) {
                count = 0;
                q.pop();
                i += 1;
            } else {
                int x = q.front();
                q.pop();
                q.push(x);
                count += 1;
            }
        }

        return q.size();
    }
};