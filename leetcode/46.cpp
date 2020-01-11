class Solution {
public:
    void possible( vector<vector<int>>& permutes, int n, vector<int>&nums){
        if (n==nums.size()){
            permutes.push_back(nums);
            return;
        }
        // nth value swap and dfs
        vector<int> temp = nums;
        for(int i=n; i< nums.size(); i++){
            swap(temp[n], temp[i]);
            possible(permutes,n+1, temp);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> permutes;
        
        possible(permutes, 0, nums);
        
        return permutes;
    }
};
