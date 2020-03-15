// 937. Reorder Data in Log Files

// Solution 1 - Beat 64.46%
// Using DP table.
// First, find the [0,i] longest subsequence (which includes ith value)
// Second, looping through 0~N, find the longest subsequence value. 
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int N = nums.size();
        if(N==0)
            return 0;
        int * dp = new int[N];
        for(int i =0; i<N; i++){
            dp[i] = 1;
        }
        
        for(int i = 1;i<N; i++){
            // find dp[i]
            int max = 1;
            for(int j=0; j< i; j++){
                if(nums[j] < nums[i]){
                    if (max < dp[j] + 1)
                        max = dp[j]+1;
                }
            }
            dp[i] = max;
        }
        int maxlen= 1;
        for(int i =0; i<N; i++){
            if(maxlen < dp[i])
                maxlen = dp[i];
        }
        
        return maxlen;
    }
};
