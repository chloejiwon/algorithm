class Solution {
public:
    bool isValid(string s) {
        stack<char> st;
        int pair[3];
        if(s.length() %2 ==1)
            return false;
        for(int i=0; i<s.length(); i++){
            char tmp;
            if(s[i] == '(' || s[i] == '[' || s[i] == '{'){
                st.push(s[i]);
            }else if(s[i] == ')'){
                if(st.empty())
                    return false;
                tmp = st.top();
                st.pop();
                if (tmp != '(')
                    return false;
            }else if(s[i]==']'){
                if(st.empty())
                    return false;
                tmp = st.top();
                st.pop();
                if (tmp != '[')
                    return false; 
            }else if(s[i] == '}'){
                 if(st.empty())
                    return false;
                tmp = st.top();
                st.pop();
                if (tmp != '{')
                    return false;
            }
        }
        if (st.empty())
            return true;
        else
            return false;
    }
};
