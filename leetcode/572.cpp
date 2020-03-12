// 572. Subtree of Another Tree

// Solution 1 - Beat 77.23%
// Needed debugging :( 
// Try to solve it at once. (not run and debug)
// Think of a simple solution first.
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
    bool cmp(TreeNode *s, TreeNode *t,bool valueCheck){
        bool isSubtree = false;
        if(s == NULL && t == NULL)
            return true;
        if(s==NULL || t==NULL)
            return false;
        
        if(valueCheck){
            if (s->val != t->val)
                return false;
            if(cmp(s->left,t->left,true) && cmp(s->right,t->right,true))
                return true;
        }
        else {
            if(s->val == t->val){
                if (cmp(s->left,t->left,true) && cmp(s->right,t->right,true))
                    return true;
            }
            if(cmp(s->left,t,false))
                return true;
            if(cmp(s->right,t,false))
                return true;
        }
        return false;
    }
    bool isSubtree(TreeNode* s, TreeNode* t) {
        return cmp(s,t,false);
    }
};
