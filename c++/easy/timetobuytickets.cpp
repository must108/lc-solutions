#include <iostream>

class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int count = 0;
        int vectLen = tickets.size();
        int pos = tickets[k];
        int seconds = 0;
        while(count < pos) {
            for(int i = 0; i < vectLen; i++) {
                if(tickets[i] > 0 && tickets[k] != 0) {
                    tickets[i] -= 1;
                    seconds += 1;
                } else if(tickets[k] == 0) {
                    break;
                }
            }
            count += 1;
        }

        return seconds;
    }
};