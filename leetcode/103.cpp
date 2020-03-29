/*
 * 103. Binary Tree Zigzag Level Order Traversal
 */

#include <iostream>
#include <vector>
#include <queue>

using namespace std;

 // Definition for a binary tree node.
 struct TreeNode {
      int val;
      TreeNode *left;
      TreeNode *right;
      TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
 
// Solution 1 
// BFS - faster than 84.20%
// use Reverse function.
class Solution {
public:
    vector< vector<int> > zigzagLevelOrder(TreeNode* root) {
        vector< vector<int> > res;
        queue< TreeNode * > q;
        if (root)
            q.push(root);
        bool rtol = false;
        while(!q.empty()){
            vector<int> tmp; int size = q.size();
            for(int i=0; i<size; i++){
                TreeNode * cur = q.front(); q.pop();
                tmp.push_back(cur->val);
                if(cur->left)
                    q.push(cur->left);
                if(cur->right)
                    q.push(cur->right);
            }
            if(rtol){
                reverse(tmp.begin(),tmp.end());
            }
            res.push_back(tmp);
            rtol = !rtol;
        }
     
        return res;
    }
};

int main(){
    Solution sol;

    return 0;
}