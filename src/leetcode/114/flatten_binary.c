/*
 * =====================================================================================
 *
 *       Filename:  flatten_binary.c
 *
 *    Description: flatten binary tree to linked list; leetcode # 114
 *
 *        Version:  1.0
 *        Created:  11/01/2018 07:33:17 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *
 * =====================================================================================
 */
#include <stdlib.h>

struct TreeNode {
        int val;
        struct TreeNode *left;
        struct TreeNode *right;
};

void flatten(struct TreeNode* root){
    struct TreeNode *old_right;
    struct TreeNode *old_left;
    struct TreeNode *traverse;

    if (root == NULL) {
        return;
    }

    old_left = root->left;
    old_right = root->right;

    root->left = NULL;
    flatten(old_left);
    flatten(old_right);

    root->right = old_left;

    traverse = root;
    while (traverse->right != NULL) {
        traverse = traverse->right;
    }
    traverse->right = old_right;
}
