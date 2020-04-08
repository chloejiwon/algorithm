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

    int solve(int conyPosition, int brownPosition) {
        int time = 0;
        bool visit[200001][2];
        queue<pair<int, int> > queue;
        memset(visit, 0, sizeof(visit));
        queue.push(make_pair(brownPosition, 0));
        while (1) {
        conyPosition += time;
            if (conyPosition > 200000)
                return -1;
            if (visit[conyPosition][time % 2])
                return time;
            for (int i = 0, size = queue.size(); i < size; i++) {
                int currentPosition = queue.front().first;
                int newTime = (queue.front().second + 1) % 2;
                int newPosition;
                queue.pop();
                newPosition = currentPosition - 1;
                if (newPosition >= 0 && !visit[newPosition][newTime]) {
                    visit[newPosition][newTime] = true;
                    queue.push(make_pair(newPosition, newTime));
                }
                newPosition = currentPosition + 1;
                if (newPosition < 200001 && !visit[newPosition][newTime]) {
                    visit[newPosition][newTime] = true;
                    queue.push(make_pair(newPosition, newTime));
                }   
                newPosition = currentPosition * 2;
                if (newPosition < 200001 && !visit[newPosition][newTime]) {
                    visit[newPosition][newTime] = true;
                    queue.push(make_pair(newPosition, newTime));
                }
            }
            time++;
        }
    }
};
int main(){
    int C, B;
    //cin >> C >> B ;
    C = 1; B = 2;
    Solution sol;
    //cout << sol.solution(C,B) << endl;

    cout << sol.solve(C,B) << endl;
    return 0;
}