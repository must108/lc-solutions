#include <iostream>

class Solution {
public:
    int sumNumbers(TreeNode* root) {
        return help(root, 0);
    }

    int help(TreeNode* root, int currSum) {
        if(root == NULL) return 0;
        currSum = currSum * 10 + root->val;
        if(root->left == NULL && root->right == NULL) return currSum;
        return help(root->left, currSum) + help(root->right, currSum);
    }
};