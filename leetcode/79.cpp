// 이것은...디버깅의승리...?;;;

// 79. Minimum Window Substring
// Solution 1 - Sliding window --- Beat 20%

// need to work on simplifying methods.. 

// if s[start] is not substr in T, start++;
// if s[start~end] contains all chars in T 
//      if start-end+1 < min_len, min_len = start-end+1
//      if not, start ++;
// if not, start ++; 

class Solution {
public:
    string minWindow(string s, string t) {
        int window_end = 0; 
        int min_size = t.length();
        if (min_size == 0)
            return "";
        
        vector<int> a(58);
        for(int k=0; k<min_size; k++){
            a[t[k]-65]++;
        }
        vector<int> b(58);
        b[s[0]-65]++;
        int i=0; int j=0; int minLen = 999999;
        int start = 0; int end = 0;
        int total = s.length();
        while(j < total && i < total)
        {
            if(a[s[i]-65] == 0 )
            {
                b[s[i]-65]--;
                i++; 
                continue;
            }
            if(a[s[j] - 65] > 0 )
            {
                bool everychar = true;
                for(int k=0; k<58; k++)
                {
                    if(a[k] >0 && b[k] < a[k])
                    {
                        everychar = false;
                        break;
                    }
                }
                if(everychar)
                {
                    if(minLen > j - i +1)
                    {
                        minLen = j-i+1;
                        start = i; end = j;
                    }
                    b[s[i]-65]--;
                    i++;
                }
                else
                {
                    j++;
                    if(j < total) b[s[j]-65]++;
                }
            }
            else
            {
                j++;
                if(j < total) b[s[j]-65]++;
            }
        }
        if(minLen < 999999)
            return s.substr(start,minLen);
        else
            return "";
    }
};
