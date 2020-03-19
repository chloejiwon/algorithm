// 62. Unique Paths 


// Making DP table  int [][] - Beat 100%
class Solution {
public:
    int uniquePaths(int m, int n) {
        /*int ** dp;
        // initialize dp table 
        dp = new int *[n];
        for(int i=0; i<n; i++)
            dp[i] = new int[m];*/
        
        
        int dp[100][100];
        
        for(int i = 0; i<m; i++)
            dp[0][i] = 1;
        for(int i=0; i<n; i++)
            dp[i][0] = 1;
        for(int i=1; i<n; i++){
            for(int j=1; j<m; j++){
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        
        return dp[n-1][m-1];
    }
};
