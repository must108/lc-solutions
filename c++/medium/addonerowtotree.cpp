#include <iostream>

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if(root == NULL) return NULL;
        
        if(depth == 1) {
            TreeNode *temp = new TreeNode(val);
            temp->left = root;
            return temp;
        }

        if(depth == 2) {
            TreeNode *left = new TreeNode(val);
            TreeNode *right = new TreeNode(val);

            right->right = root->right;
            right->left = nullptr;
            left->left = root->left;
            left->right = nullptr;

            root->right = right;
            root->left = left;

            return root;
        }

        addOneRow(root->left, val, depth - 1);
        addOneRow(root->right, val, depth - 1);

        return root;
    }
};