// 1007. Minimum Domino Rotations For Equal Row

// Solution 1  - Beat 63%
// Brute Force
// Time Complexity : O(N*N)

class Solution {
public:
    int minDominoRotations(vector<int>& A, vector<int>& B) {
        int minA =0, minB = 0;
        
        int counterA[7]= {0,};
        for(auto t : A){
            counterA[t] ++;
        }
        int maxVal = 0;
        bool visited[7] = {false,};
        while(1){
            // find Max value
            minA = 0;
            maxVal = 0;
            int idx = 0;
            for(int i =1; i<7; i++){
                if(maxVal < counterA[i] && visited[i]==false){
                    maxVal = counterA[i];
                    idx = i;
                }
            }
            
            if(idx == 0)
                break;
            if(counterA[idx]==A.size())
                return 0;
            
            visited[idx] = true;
            
            bool possible = true;
            for(int i=0; i<A.size();i++){
                if(A[i] != idx){
                    if(B[i] == idx){
                        minA++;
                    } else{
                        possible =false;
                        break;
                    }
                }
            }
            if(possible)
                break;
        }
        int counterB[7] = {0,};
        for(auto t:B){
            counterB[t]++;
        }
        bool visited2[7] = {false,};
        while(1){
            // find Max value
            minB = 0;
            maxVal = 0;
            int idx = 0;
            for(int i =1; i<7; i++){
                if(maxVal < counterB[i] && visited2[i] == false){
                    maxVal = counterB[i];
                    idx = i;
                }
            }
            if(idx == 0)
                break;
            if(counterB[idx]==B.size())
                return 0;
            
            visited2[idx] = true;
            bool possible = true;
            for(int i=0; i<B.size();i++){
                if(B[i] != idx){
                    if(A[i] == idx){
                        minB++;
                    } else{
                        possible =false;
                        break;
                    }
                }
            }
            if(possible)
                break;
        }
        if (minA == 0 && minB == 0)
            return -1;
        if(minA ==0 )
            return minB;
        if(minB==0)
            return minA;
        if(minA < minB)
            return minA;
        else
            return minB;
    }
};

