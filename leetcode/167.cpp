// 167. Two Sum 2 - Input array is sorted

// Solution 1
// Brute force approach - Beat 6% 
class Solution {
public:
    int findIndex2(vector<int>& numbers,int target, int start){
        int res = -1;
        for (int i=start; i<numbers.size(); i++){
            if(numbers[i] > target)
                break;
            if(numbers[i] == target){
                res = i+1;
                break;
            }
        }
        return res;
    }
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector <int> res;
        for(int i=0; i<numbers.size(); i++){
            int j = findIndex2(numbers,target-numbers[i],i+1);
            if(j!= -1){
                res.push_back(i+1);
                res.push_back(j);
                break;
            }
            
        }
        return res;
    }
};
