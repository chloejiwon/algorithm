class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        if(nums.size() == 0)
            return 0;
        map<int,int> m;
        for(auto & num : nums){
            m[num]++;
        }
        k = nums.size() - k +1 ; 
        for(auto &iter :m){
            k -= iter.second;
            if(k <= 0)
                return iter.first;
        }
        return 0;
        
    }
};