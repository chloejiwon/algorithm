class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        
        int N = A.size();
        int result = 0;
        unordered_map<int,int> ab; 
        for(auto i : A){
            for(auto j : B){
                ab[i+j]++;
            }
        }
        for (auto i : C){
            for(auto j : D){
                //find sum of ab * (-1) == C[i] + D[j];
                if(ab.find(-(i+j))!=ab.end())
                    result += ab[-(i+j)]; 
            }
        }
        return result;
        
    }
};
