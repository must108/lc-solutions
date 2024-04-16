#include <iostream>

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* reversed = nullptr;

        while(head != nullptr) {
            ListNode* nextNode = head->next;
            head->next = reversed;
            reversed = head;
            head = nextNode;
        }

        return reversed;
    }
};