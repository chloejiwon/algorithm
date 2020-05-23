// you can use includes, for example:
// #include <algorithm>

// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

#define MAX_INT 2147483647
bool bsearch(const vector<int> &A, int K, int largeSum){
    
    int N = A.size(); int j=0; long long sum=0;
    for(int i=0; i<N; i++){
        sum += A[i];
        if(sum > largeSum){
            j++;
            if (j > (K-1)) return false;
            sum =A[i];
        }
    }
    
    return true;
}
int solution(int K, int M, vector<int> &A) {   
    // write your code in C++14 (g++ 6.2.0)
    int minMax=0;
    if(K==1){
        int sum = 0;
        for(auto a:A){sum += a;}
        return sum;
    }
    int largeSum = 0; int N = (int)A.size();
    for(int i=0; i<N; i++) largeSum += A[i];
    
    int arrMax = 0; 
    for(int i=0; i<N; i++) arrMax = max(arrMax, A[i]);
    
    if(K==N)
        return arrMax;
        
    int low = arrMax; int end = largeSum;
    if(low > end) swap(low,end);
    minMax = largeSum;
    while(low <= end){
        int mid = (low+end)/2;
        if(bsearch(A, K, mid)){
            end = mid - 1;
            minMax = mid;
        }else{
            low = mid + 1;
        }
    }
    return minMax;
}
