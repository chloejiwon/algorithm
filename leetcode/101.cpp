// 101. Symmetric Tree


// Solution 1 - Recursion, Beat 83.84%
// Time Complexity : O(n) because we traverse the entire input tree once.
// n = total number of nodes in the tree
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSame(TreeNode * a, TreeNode * b){
        // make sure a and b are symmetric.
        // if not, return false
        if(a == NULL && b==NULL)
            return true;
        else if(a!= NULL && b == NULL)
            return false;
        else if(a== NULL && b!=NULL)
            return false;
        
        if(a->val != b->val )
            return false;
        
        return isSame(a->left,b->right) & isSame(a->right,b->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(root==NULL)
            return true;
        return isSame(root->left, root->right);
            
    }
};
