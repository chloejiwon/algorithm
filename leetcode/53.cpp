class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int * dp = new int[nums.size()+1];
        int sum = 0;
        dp[0] = nums[0];
        int n = nums.size();
        for(int i=1; i<n; i++){
            dp[i] = max(dp[i-1]+nums[i], nums[i]);
        }
        // find the maximum value
       sum =  dp[0];
        for(int i=1; i<n; i++){
            if (sum < dp[i]) sum = dp[i];
        }
        delete []dp;
        return sum;
    }
};
