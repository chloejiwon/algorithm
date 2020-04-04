
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;


class Solution{
    public:
    bool binarySearch(int N, vector<int> &a, int target){
        // a is sorted array.
        int start = 0; int end = N-1;
        while(start <= end){
            int mid = (start + end ) / 2;
            if(a[mid] < target){
                start = mid + 1;
            }else if(a[mid] > target){
                end = mid - 1;
            }else{
                return true;
            }
        }
        return false;
    }
    void solve(int N, vector<int> & a, int M, vector<int> & b){
        sort(a.begin(), a.end());
        // Binary Search!!
        for(int i=0; i<M; i++){
            if(binarySearch(N, a, b[i]))
                printf("1\n");
            else 
                printf("0\n");
            
        }
        
    }

};
int main(){
    Solution sol;
    int n,m; vector<int> A,B;
    scanf("%d",&n); int tmp = 0;
    for(int i=0; i<n; i++){
        scanf("%d", &tmp);
        A.push_back(tmp);
    }

    scanf("%d", &m);
    for(int i=0; i<m; i++){
        scanf("%d", &tmp);
        B.push_back(tmp);
    }

    sol.solve(n,A,m,B);
    return 0;
}