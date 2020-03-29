#include <iostream>
#include <vector>
#include <map>

using namespace std;

// 739. Daily Temperatures

// Solution 1 - Greedy algorithm - TIME LIMIT EXCEDDED!!!!
// Time Complexity O(N*N)
/* 
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        // T length 1 ~ 30000
        // 30 <= each temperature <= 100
        int T_len = T.size();
        vector<int> days(T_len,0);
        for(int i=0; i<T_len; i++){
            int cnt = 1; bool is_found = false;
            for(int j=i+1; j<T_len; j++){
                if(T[i] < T[j]){
                    is_found = true; break;
                }else{
                    cnt ++;
                }
            }
            if (is_found)
                days[i]  =cnt;
            else
                days[i] = 0;
        }
        return days;
    }
};
*/

// Solution 2 - using Hashtable --> Time Limit Exceeded!!
#if 0
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        // T length 1 ~ 30000
        // 30 <= each temperature <= 100
        int T_len = T.size();
        vector<int> days(T_len,0);
        
        map<int, vector<int>> m;
        for(int i=0; i<T_len; i++)
            m[T[i]].push_back(i);
        
        for(int i=0; i<T_len;i++){
            int j = 1;
            bool isFound = false; int day = 0;
            while(T[i] + j <= 100 && !isFound){
                if(m.find(T[i]+j)){
                    vector<int> items = m[T[i]+j];
                    for(auto &item : items){
                        if(i < item){
                            isFound = true;
                            day = item-i+1;
                            break;
                        }
                    }
                } else {
                    j++;
                }
                
            }
            if (isFound)
                days[i] = day;
        }

        return days;
    }
};
#endif

// Solution 3 - Using Stack! - faster than 32.40%
// TimeComplexity O(N)
/* ************************
1. Iterate backwards. keep track of warmer temp.
2. if current temp >= stack's warmer temp, pop warmer temp and put current temp.
we don't need stack's warmer temp any more.
b/c nearer warmer temp is there. 
3. if current temp < stack's warmer temp, day[i] = stack's warmer temp day - i;
*************************** */
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        // T length 1 ~ 30000
        // 30 <= each temperature <= 100
        vector<int> days(T.size(),0);
        stack<int> s;
    
        for(int i=T.size()-1; i>=0;i--){
            while(!s.empty() && T[i] >= T[s.top()]){
                s.pop();
            }
            if(!s.empty())
                days[i] = s.top() - i;
            s.push(i);
        }

        return days;
    }
};

int main(){
    Solution sol;
    vector<int> T;
    cout << sol.dailyTemperatures(T) << endl;
    return 0;
}