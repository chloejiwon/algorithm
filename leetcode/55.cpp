// 55. Jump Game

// Solution 1 - Time Limit Exceeded
// For test case [8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]
// using queue, store next jumpable step 
// if reach last index, return true
// if not reach iterate whole queue, and if queue is empty, return false
class Solution {
public:
    bool canJump(vector<int>& nums) {
	queue<int> q;
	q.push(0);
	while(!q.empty()){
		int idx = q.front();
		q.pop();
		for(int i =1; i<=nums[idx] ;i++){
			if( i+idx < nums.size()){
				// reached last index
				if(i+idx == nums.size()-1)
					return true;
				if(i!=0)
					q.push(i+idx);
			}
		}
	}
	return false;   
    }
};


// Solution 2 - Beat 11.11%
// Same method, but adding visited array and for loop sequence reverse
class Solution {
public:
    bool canJump(vector<int>& nums) {
        queue<int> q;
        int N = nums.size();
        q.push(0);
        bool * visited = new bool[N+1];
        for(int i=0; i<N; i++)
            visited[i] = false;
        while(!q.empty()){
                int idx = q.front();
                q.pop();
                
                if(visited[idx] == false){
                    visited[idx] = true;
                    for(int i =nums[idx]; i>=0;i--){
                            if( idx + i < N){
                                    // reached last index
                                    if(idx + i == N-1){
                                        return true;
                                    }
                                    if(i!=0 && visited[idx+i] == false)
                                        q.push(idx + i);
                            }
                    }
                }
        }
        return false;
    }
};


// Solution 3 - Beat 8%
// Using DFS method
class Solution {
public:
    bool *visited;
    bool dfs(vector<int> & nums, int idx, int N){
        if(visited[idx] == false){
            visited[idx] = true;
            for(int i=nums[idx]; i>=0 ; i--){
                if (idx+i == N-1){
                    return true;
                }
                if (idx+i < N){
                    if(dfs(nums,idx+i, N))
                        return true;
                }
            }
        }
        return false;
    }
    bool canJump(vector<int>& nums){
        // start from maximum length ~ 0
        int N = nums.size();
        visited = new bool[N+1];
        for(int i=0; i<N; i++)
            visited[i] = false;
        
        return dfs(nums,0,N);
    
    } 
};

// Soltuion 4 - 97%
// Using DP 
// Time Complexity : O(n) 
class Solution{
public:
        bool canJump(vector<int> &nums){
            int idx = 0;
            for(int i = nums.size()-1; i>=0; i--){
                if(i + nums[i] >= idx)
                    idx = i;
            }
            
            return idx == 0;
        }
};
