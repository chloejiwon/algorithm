#include <iostream>
#include <map>
#include <vector>

using namespace std;

class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        if(nums.size() == 0)
            return 0;
        map<int,int> m;
        for(int & num : nums){
            m[num]++;
        }
        k = nums.size() - k +1 ; 
        for(auto iter = m.begin(); iter != m.end(); iter++){
            k -= iter->second;
            if(k <= 0)
                return iter->first;
        }
        return 0;
        
    }
};

int main(){
    Solution sol;
    vector<int> nums{1,3,4,2,3,1};
    int k = 2;
    cout << sol.findKthLargest(nums, k) << endl;
    return 0;
}