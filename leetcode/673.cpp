// 673. Number of Longest Increasing Subsequence

// Solution 1 - Beat 24.55%
// Based on LIS, 
// Make one more table to keep number of LIS
class Solution {
public:
    int findNumberOfLIS(vector<int>& nums) {
        int N = nums.size();
        if (N == 0)
            return 0;
        int * dp = new int[N];
        int * dp2 = new int[N];
        dp2[0] = 1; dp[0] = 1; int max_len = 1;
        int res = 0;
        for(int i=1; i<N; i++){
                int max = 1;
                int cnt = 1;
                for(int j=0; j<i; j++){
                        if(nums[j] < nums[i]){
                                if (max == dp[j]+1){
                                        cnt += dp2[j];
                                }
                                if(max < dp[j]+1) {
                                        max = dp[j]+1;
                                        cnt = dp2[j];
                                }

                        }
                }
                dp[i] = max;
                dp2[i] = cnt;
                if(max_len < dp[i]){
                    max_len = dp[i];
                    res = dp2[i];
                }else if(max_len == dp[i]){
                    res += dp2[i];
                }
        }
        if(max_len == 1){
            return N;
        }
        return res;
    }
};

