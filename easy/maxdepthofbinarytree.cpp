#include <iostream>

class Solution {
public:
    int maxDepth(TreeNode* root) {
        int left = 0, right = 0;
        if(root == nullptr) {
            return 0;
        }

        if(root->left != NULL) {
            left =  1 + maxDepth(root->left);
        } else {
            left += 1;
        }

        if(root->right != NULL) {
            right = 1 + maxDepth(root->right);
        } else {
            right += 1;
        }

        return max(left, right);
    }
};