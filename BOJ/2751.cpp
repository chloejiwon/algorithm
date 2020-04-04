
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
            while(a[i] < pivot ) i++;
            while(a[j] > pivot) j--;   
            
            if(i <= j){
                swap(a[i], a[j]);
                i++; j--;
            }
        }
        if (left < j)
            quickSort(a, left, j);
        if (i < right)
            quickSort(a, i, right);
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
    sol.quickSort(A, 0, n-1);
    for(int i=0; i<n; i++){
        printf("%d\n", A[i]);
    }
    return 0;
}