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


// Solution 2 
// Binary Search - Beat 50.85%
class Solution {
public:
    // binary search
    int binarySearch(vector<int>& numbers,int target, int start,int end){
        int res = -1;
        
        if(numbers[start] > target)
            return res;
        
        while(start < end){
            int mid = (end + start)/2;
            if (numbers[mid] < target){
                start = mid + 1;
            } else if(numbers[mid] > target) {
                end = mid;
            } else {
                res = mid;
                break;
            }
        }
        
        
        return res;
    }
    vector<int> twoSum(vector<int>& numbers, int target) {
        vector <int> res;
        int N = numbers.size();
        for(int i=0; i<N; i++){
            int j = binarySearch(numbers,target-numbers[i],i+1,N);
            if(j!= -1){
                res.push_back(i+1);
                res.push_back(j+1);
                break;
            }
            
        }
        return res;
    }
};
