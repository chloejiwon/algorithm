// 2493. TOP

#include <stdio.h>
#include <stack>

using namespace std;

class Solution{
    public:
    void solve(int N, int building[]){
        stack<int> s;
        for(int i=0; i<N; i++){
            if(i==0){
                printf("0 "); s.push(i);
                continue;
            } else {
                while(!s.empty() && building[s.top()] < building[i]){
                    s.pop();
                }
                if(s.empty()){
                    printf("0 ");
                }else{
                    printf("%d ",s.top()+1);
                }

                s.push(i);

            }
        }
    }
};
int main(){
    Solution sol;
    int N; int arr[500001];
    scanf("%d",&N);
    for(int i=0; i<N;i++)
        scanf("%d",&arr[i]);

    sol.solve(N,arr);
    return 0;
}