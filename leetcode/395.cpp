class Solution {
public:
    int solve(string& s, int l, int r, int k){
        bool flag = true;
        int result = 0;
        int end =l;
        vector<int> count(26,0);
        for(int i=l; i<=r; i++){
            count[s[i]-'a']++;
        }
        for(int i=0; i<26 && flag; i++){
            if (count[i]>0 && count[i]<k){
                flag = false;
            }
        }
        if(flag) {
            return (r-l+1);
        }
        int i = l;
        for(int j=l; j<=r; j++){
            if(count[s[j]-'a']>0 && count[s[j]-'a'] < k){
                result = max(result, solve(s,i,j-1,k));
                i = j+1;
            }
        }
        
        return max(result, solve(s,i,r,k));        
    }
    int longestSubstring(string s, int k) {
        int n = s.size();
        return solve(s,0,n-1, k);
    }

};
