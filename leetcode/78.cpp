# Solution 1  - Bit Manipulation - beat 94.61%

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // Let's practice bit manipulation
        vector<vector<int>> res;
        int total = nums.size();
        for(int i=0; i< (1<<total) ; i++){
            vector<int> tmp;
            int j = i; int cnt = 0;
            while(j > 0 && cnt < total){
                if(j&1){
                    tmp.push_back(nums[cnt]);
                }
                j = j>>1;cnt++;
            }
            res.push_back(tmp);
        }
        
        return res;
    }
};
