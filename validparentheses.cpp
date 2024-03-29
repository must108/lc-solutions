#include <iostream>

typedef struct stck {
    char data;
    struct stck *next;
} stck;

int empty(stck* front) {
    if(front == NULL) return 1; else return 0;
}

char pop(stck** front) {
    if(!empty(*front)) {
        stck* temp = *front;
        *front = (*front)->next;

        char ret = temp->data;
        return ret;
    }

    return 'I';
}

int push(stck** front, char c) {
    stck *temp = new stck;

    if(temp != NULL) {
        temp->data = c;
        temp->next = *front;
        *front = temp;
        return 1;
    }

    return 0;
}

void init(stck** front) {
    *front = NULL;
}

class Solution {
public:
    bool isValid(string s) {
        int valid;
        stck *check = NULL;

        init(&check);

        for(int i = 0; i < s.length(); i++) {
            if(s.length() < 2) {
                return false;
            }

            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
                push(&check, s[i]);
            } else if(s[i] == ')') {
                char a = pop(&check);
                if(a == 'I' || a != '(') {
                    valid = 0;
                    return false;
                }
            } else if(s[i] == '}') {
                char a = pop(&check);
                if(a == 'I' || a != '{') {
                    valid = 0;
                    return false;
                }
            } else if(s[i] == ']') {
                char a = pop(&check);
                if(a == 'I' || a != '[') {
                    valid = 0;
                    return false;
                } 
            }
        }

        if(pop(&check) != 'I') {
            valid = 0;
            return false;
        }

        return true;
    }
};