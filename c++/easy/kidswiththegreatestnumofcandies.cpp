#include <iostream>

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        vector<bool> retArray = {};
        bool checker = true;

        for(int i = 0; i < candies.size(); i++) {
            for(int j = 0; j < candies.size(); j++) {
                if(candies[i] + extraCandies >= candies[j]) {
                    checker = true;
                } else {
                    checker = false;
                    break;
                }
            }

            retArray.push_back(checker);
        }

        return retArray;
    }
};