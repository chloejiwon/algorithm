
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> m;
        for(int i: nums){
            m[i]++; // watch out this !!!!! i is not index!!!!
        }
        
        vector<int> res;
        priority_queue<pair<int, int>> pq;
        for(auto it= m.begin(); it!=m.end() ;it++){
                pq.push(make_pair(it->second, it->first));
        }
        for(int i = 0; i<k; i++){
            res.push_back(pq.top().second);
            pq.pop();
        }
        return res;
    }
};
