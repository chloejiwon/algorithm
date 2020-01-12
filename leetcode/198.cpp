class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.size() == 0 )
            return 0;
        int * dp = new int[nums.size()];
        bool * flag = new bool[nums.size()];
        dp[0] = nums[0]; flag[0] = true;
        for(int i=1; i<nums.size(); i++){
            if(i==1){
                if( dp[0] < nums[i]){
                    dp[1] = nums[1]; flag[1] = true;
                }else{
                    dp[1] = dp[0];flag[1] = false;
                }
            }
            else{
                if(flag[i-1]==true){
                    if(dp[i-2]+nums[i] < dp[i-1]){
                        flag[i] = false; dp[i] = dp[i-1];
                    }else {
                        flag[i] = true; dp[i] = dp[i-2]+nums[i];
                    }
                }
                else {
                    dp[i] = dp[i-1] + nums[i]; flag[i] = true;
                }
            }
        }
        // find maximum 
        int maxmoney = 0;
       for(int i=0; i<nums.size(); i++){
           maxmoney = max(maxmoney, dp[i]);
        }
        return maxmoney;
    }
};
