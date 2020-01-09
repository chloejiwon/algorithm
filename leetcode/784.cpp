class Solution {
public:
    void dfs(string S, vector<string>&v, int idx) {
        v.push_back(S);
        if (idx >= S.length())
            return;
        for(int i=idx; i<S.length(); i++){
            if (isalpha(S[i])){
                S[i] ^= 32;
                dfs(S, v, i+1);
                S[i] ^= 32;
            }
        }
    }
    vector<string> letterCasePermutation(string S) {
        vector<string> v;
        dfs(S, v, 0);
        return v;
    }
};
