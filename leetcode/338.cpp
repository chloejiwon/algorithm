// 338. Counting Bits


// Solution 1 - 83.7%
// keep in mind that if num%2==0, num = (num/2)*2. So, dp[num] = dp[num/2]
// Otherwise, dp[num] = dp[num/2]+1
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> dp;
        for(int i =0; i<=num; i++)
            dp.push_back(0);
        
        dp[0] = 0; 
        if (num >= 1)
            dp[1] = 1; 
        if (num >= 2)
            dp[2] = 1;
        
        for(int i = 3; i<=num; i++){
            if(i%2 ==1)
                dp[i] = dp[i/2] + 1;
            else
                dp[i] = dp[i/2];
            
        }
        
        
        return dp;
        
    }
};
