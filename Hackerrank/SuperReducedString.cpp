#include <bits/stdc++.h>

using namespace std;

// Complete the superReducedString function below.
string superReducedString(string s) {
    string res = "";
    int len = s.length();
    bool isFound = false;
    for(int i=0; i<len;){
        int j=i+1;
        while(j<len && s[j]==s[i]){
            j++; isFound = true;
        }
        if( (j-i)%2 == 1 ){
            res.append(s.substr(i,1));
        }
        i = j;
    }
    if(res == "")
        return "Empty String";

    cout << res;

    if(isFound)
        return superReducedString(res);
    else 
        return res;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    string result = superReducedString(s);

    fout << result << "\n";

    fout.close();

    return 0;
}
