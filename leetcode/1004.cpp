// 1004. Max Consecutive Ones III

// Need to solve one more time!!!
class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int i=0; int j=0;
        for(j=0; j<A.size(); j++){
            if (A[j] == 0 )K--;
            if (K<0){
                if(A[i]==0)
                    K++;
                i++;
            }
        }
        return j-i;
    }
};
