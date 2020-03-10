# Solution 3 - Using CPP

# Beat 94.78 %
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        if(grid.empty()) return 0;
        int N = grid.size(), M = grid[0].size();
        queue<int> q;
        int oranges =0;
        for (int i =0 ;i<N;i++){
            for (int j=0 ; j<M; j++){
                if(grid[i][j] == 2)
                    q.push(i*M + j);
                else if (grid[i][j] == 1)
                    oranges++;
            }
        }
        if (oranges == 0) return 0;
        int ans=0,cnt = 0;
        
        vector<vector<int>> dir = {{0,1},{0,-1},{1,0},{-1,0}};
        while(!q.empty()){
            ans ++;
            int size = q.size();
            for (int j = 0; j<size; j++){
                int loc = q.front();
                q.pop();
                int x = loc / M;
                int y = loc % M;
                for (int i =0; i<4; i++){
                    int nx = x + dir[i][0];
                    int ny = y + dir[i][1];
                    if (nx >=0 && nx < N && ny >=0 && ny < M){
                        if(grid[nx][ny]==1){
                            cnt ++;
                            grid[nx][ny]=2;
                            if(cnt == oranges)
                                return ans;
                            q.push(nx*M+ny);
                        }
                    }
                }
               
            }
        }
        if(cnt != oranges)
            return -1;
        return ans;
    }
};
