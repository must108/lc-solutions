#include <iostream>

class Solution {
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        if(root == NULL) return false;
        if(root->val == targetSum && root->left == NULL && root->right == NULL) return true;
        if(root->left != NULL) root->left->val += root->val;
        if(root->right != NULL) root->right->val += root->val;
        return hasPathSum(root->left, targetSum) || hasPathSum(root->right, targetSum);
    }
};