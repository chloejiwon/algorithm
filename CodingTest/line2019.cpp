#include <iostream>
#include <vector>
#include <queue>

using namespace std;

#define MAX_LENGTH 2000000

class Solution{
    public :
        int solution(int coniPosition, int BrownPosition) {
            int time = 0;
            queue<int> q;
            q.push(BrownPosition);
            bool gotConi = false;
            while(!q.empty() && !gotConi && coniPosition <= MAX_LENGTH){
                int size = q.size();
                //cout << "Current Time " << time << endl;
                bool visit[MAX_LENGTH + 1];
                memset(visit, 0, sizeof(visit));

                for(int i = 0; i<size; i++){
                    int cur = q.front();
                    //cout << "Coni Pos : " << coniPosition << " Brwon Pos : " << cur << endl;
                    q.pop();
                    if(visit[cur]) continue;
                    visit[cur] = true;
                    if(cur == coniPosition){
                        gotConi = true; break;
                    }
                    
                    // Push every possible move to go!
                    int next_mv = 0;

                    next_mv = cur -1;
                    if(next_mv <= MAX_LENGTH && next_mv >=0 ) q.push(next_mv);
                    next_mv = cur + 1;
                    if(next_mv <= MAX_LENGTH && next_mv >=0 ) q.push(next_mv); 
                    next_mv = cur * 2;
                    if(next_mv <= MAX_LENGTH && next_mv >=0 ) q.push(next_mv);
                    
                }
                if(!gotConi)
                    coniPosition += (time++) + 1; 
            }
            if(gotConi)
                return time;
            else
                return -1;
        }
};
int main(){
    int C, B;
    //cin >> C >> B ;
    C = 11; B = 2;
    Solution sol;
    cout << sol.solution(C,B) << endl;
    return 0;
}