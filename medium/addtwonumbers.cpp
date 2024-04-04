#include <iostream>

class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* list;
        ListNode** ret = &list;
        int saveVal = 0;
        while(l1 != nullptr || l2 != nullptr || saveVal) {
            int sum = (l1 ? l1->val : 0) + (l2 ? l2->val : 0) + saveVal;
            if(sum > 9) {
                saveVal = sum / 10;
                *ret = new ListNode(sum % 10);
            } else {
                saveVal = sum / 10;
                *ret = new ListNode(sum);
            }
            l1 = (l1 ? l1->next : nullptr);
            l2 = (l2 ? l2->next : nullptr);
            ret = &((*ret)->next);
        }
        
        return list;
    }
};