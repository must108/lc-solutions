#include <iostream>

class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp = head;

        while(temp != NULL && temp->next != NULL) {
            if(temp->next->val == temp->val) {
                ListNode* del = temp->next;
                temp->next = del->next;
                delete del;
            } else {
                temp = temp->next;
            }
        }
        return head;
    }
};