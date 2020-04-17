// Solution 1 - Brute Force
// Time Complexity : O(n), Space Complexity : O(n)
// beat 78.95% 

class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        // index = (index + k) % nums.size()
        int n = nums.size();
        int * tmp = new int[n+1];
        for(int i=0; i<n; i++)
            tmp[(i+k)%n] = nums[i];
        for(int i=0; i<n; i++){
            nums[i] = tmp[i];
        }
            
        
    }
};
