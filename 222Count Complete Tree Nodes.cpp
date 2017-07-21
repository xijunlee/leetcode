/*************************************************************************
	> File Name: 222.cpp
	> Author: 
	> Mail: 
	> Created Time: Fri Jul 21 10:55:58 2017
 ************************************************************************/

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
        int countNodes(TreeNode* root) {
            if(!root) return 0;
            int lh = height(root->left);
            int rh = height(root->right);     
            if(lh == rh) 
               return (1 << lh) + countNodes(root->right);  /*1(根节点) + (1<<lh)-1(完全左子树) + # of rightNode */               
            else 
               return (1 << rh) + countNodes(root->left);  /*1(根节点) + (1<<rh)-1(完全右子树) + # of leftNode*/
        }
    private:
        int height(TreeNode *root){ //get the height of a complete binary tree.
            if(!root) return 0;
            return 1 + height(root->left);
        }
    };



