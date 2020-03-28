#include <string>
#include <vector>
#include <iostream>

using namespace std;
#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 1001;
    int len = s.length();
    if(len == 0)
        return 0;
    for(int k=1; k<=len; k++){
        // k : char unit 
        vector<string> tmp; 
        int tmp_len = 0;
        for(int i=0; i<len;){
            string cur = s.substr(i,k);
            // cout << "cur : " << cur << endl;
            // compare! 
            int cnt = 1, j = i+k;
            for(j = i+k; j<len; j+=k){
                if(cur == s.substr(j,k))
                    cnt++;
                else
                    break;
            }
            i  = j;
            if(cnt != 1){
                // check cnt > 10 or... cnt >100 so on...
                if (cnt < 10)
                    tmp_len +=1;
                else if (cnt < 100)
                    tmp_len +=2;
                else if(cnt < 1000)
                    tmp_len += 3;
                else if(cnt == 1000)
                    tmp_len += 4;
                tmp_len += cur.length();
                tmp.push_back(to_string(cnt)+cur);
            } else {
                tmp_len += cur.length();
                tmp.push_back(cur);
            }
        }
        if(answer > tmp_len)
            answer = tmp_len;

    }
    
    return answer;
}

int main(){
    string input = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    int sol = solution(input);
    cout << "Min length of string is : " << sol << endl;
    return 0;
}