#include <iostream>

using namespace std;


// Solution 1 - DP + Brute Force - Beat 99.8%
// Time Complexity : O(N^3)
// Fixed DP table
// DP[i] = keeps track of longest substr with last index i. 
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int start=0; int max_len = 1;
        int N = s.length();
        if(N == 0)
            return 0;
        int * dp = new int[N];
        // dp table initialize
        for(int j=0; j<N; j++){
            dp[j] = 1;
            for(int i=start; i<j; i++){
                if(s[j] == s[i]){
                    // same character! start over
                    // make 'start' to be something not equal to s[j]!!
                    int k =0;
                    for(k=i+1; k<j; k++){
                        if(s[k]!=s[j])
                            break;
                    }
                    start = k;
                    dp[j] = j-start+1;
		    break;
                } else {
                    dp[j] ++;
                }
            }
            if(max_len < dp[j])
                max_len = dp[j];
        }
        return max_len;
    }
};
int main(){
    Solution sol;
    string s = "tmmzuxt";
    cout << sol.lengthOfLongestSubstring(s) << endl;
    return 0;
}
