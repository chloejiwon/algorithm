# Largest Time for Given Digits

## Solution 1 - 79.21%

괜히 너무 어렵게 생각한 것 같기도 하다. 🤔 좀 더 쉬운 방법으로 재시도 해보자!

핵심 idea는 Recursion이다. 

1. 첫번째 digit은 당연히 0-2까지만 가능하다. 셋 다 있는 경우 0,1,2 각 경우에 대해 재귀로 최종 결과물의 max 값을 갖도록 한다.
1. 재귀 함수에 들어가면, 두번째 digit인 경우 hour니까 24보다 작아야 한다. 만족하면 또 재귀 호출
1. 세번째 digit이면 0-5까지만 가능! 되는 것 모두 재귀 호출
1. 네번째 digit이면 방문하지 않은 나머지 원소를 넣어주고 return
1. 최종 max값에서 각 hour, min 추출해서 string으로 만들어서 return (-1이면 불가한 것이므로 return "")


### TimeComplexity : O(1)

```cpp
class Solution {
public:
    int dfs(int count, int result, vector<int>&A, vector<bool> &visited){
        
        if(count == 3) {
            for(int i=0; i<4; i++){
                if(!visited[i]){
                    return result+A[i];
                }
            }
        }
        int max_time = -1;
        if( count == 0){
            for(int i=0; i<4; i++){
                if( A[i] <= 2){
                    visited[i] = true;
                    max_time = max(max_time, dfs(count+1, result + A[i] * 60 * 10, A, visited));
                    visited[i] = false;
                }
            }           
        }
        else if (count == 1) {
            for(int i=0; i<4; i++){
                if(!visited[i]){
                    if(result + A[i] * 60  < 24 * 60){
                        visited[i] = true;
                        max_time = max(max_time, dfs(count+1, result + A[i] * 60, A, visited));
                        visited[i] = false;
                    }
                }
            }
        } else if(count == 2) {
            for(int i=0; i<4; i++){
                if(!visited[i] && A[i] <=5){
                    visited[i] = true;
                    max_time = max(max_time,dfs(count+1, result + A[i]*10, A, visited));
                    visited[i] = false;
                }
            }
        }
        return max_time;
    }
    string largestTimeFromDigits(vector<int>& A) {
        string res;
        
        int max_time = -1;
        sort(A.begin(), A.end(), greater<int>());
        
        vector<bool> visited(4);
        max_time = max(max_time, dfs(0, 0, A, visited));

        if(max_time != -1)
        {
            int h = max_time / 60;
            int m = max_time % 60;
            if(h < 10)
                res.append("0");
            res.append(to_string(h));
            res.append(":");
            if(m < 10)
                res.append("0");
            res.append(to_string(m));
        }
        
        return res;
    }
};
```