// 567. Permutation in string


// Solution1 1 - Sliding Window (Beat 99.53%)
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        
        int i =0; int j=0;
        // window size is s1.length();
        int window_size = s1.length();
        if(window_size == 0)
            return true;
        vector<int> b(26);
        for(int k=0; k<window_size; k++){
            b[s1[k] - 97]++;
        }
        vector<int> a(26);
        i = j + 1 - window_size;
        for(j=0; j<s2.length(); j++){
            
            // j - i + 1 == window_size
            // if s2[i:j] == permutation of s1, return true;
            // not, i++;
            bool found = false;
            if (i==0) {
                for(int k=i; k<i+window_size; k++){
                    a[s2[k] - 97]++;
                }
            } else if (i > 0){
                a[s2[(i-1)] - 97]--;
                a[s2[j] - 97]++;
            }
            
            if(i>=0){
                
                // compare ! 
                found = true;
                for(int k=0; k<26; k++){
                    if(a[k] != b[k]){
                        found = false;
                        break;
                    }
                }
            }
            i++;
            if(found)
                return true;
        }
        return false;
    }
};
