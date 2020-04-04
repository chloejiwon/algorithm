
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;


class Solution{
    public:
    void quickSort(vector<int> &a, int left, int right){
        int pivot = a[(left + right)/2];
        int i = left, j = right;
        while(i <= j){
            while(a[i] < pivot) i++;
            while(a[j] > pivot) j--;   
            
            if(i <= j){
                swap(a[i], a[j]);
                i++; j--;
            }
        }
        quickSort(a, left, i);
        quickSort(a, j, right);
    }
    
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
        //sort(a.begin(), a.end());
        quickSort(a, 0, N-1);
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