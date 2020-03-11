// 692. Top K Frequent Words
// Solution 1
// Brute-Force approach
// First, using map, already sort alphabetically.
// Second, Find max Value and insert them 
// Time Complexity : O(N^N)
class Solution {
public:
 
    vector<string> topKFrequent(vector<string>& words, int k) {
        
        vector<string> res;
        if(words.empty())
            return res;
        
        map<string,int> m;
        for (int i =0; i< words.size(); i++){
            if(m.count(words[i]) < 0)
                m[words[i]]=0;
            else
                m[words[i]]++;
        }
        // need to sort by value
        for(int i=0; i<k; i++){
            int max = 0; auto temp = m.begin();
            for(auto itr = m.begin();itr!=m.end();itr++ ){
                if(max < itr->second){
                    max = itr->second;
                    temp = itr;
                }
            }
            res.push_back(temp->first);
            m[temp->first] = 0;
        }
        
        return res;
    }
};
