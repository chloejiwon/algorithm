#include <stdio.h>
#include <stack>
#include <string>
#include <iostream>

using namespace std;

string solve(string input){
    string res = "";
    stack<char> s;
    for(int i=0; i<input.length(); i++){
        if(input[i] >= 'A' && input[i] <= 'Z'){
            res += input[i];
        }else{
            switch(input[i]){
                case '(':
                    s.push(input[i]);
                    break;
                case '*':
                case '/':
                    while(!s.empty() && (s.top() == '*' || s.top() == '/' )) {
                            res += s.top();
                            s.pop();
                    }
                    s.push(input[i]);
                    break;
                case '+':
                case '-':
                    while(!s.empty() && (s.top() != '(')) {
                        res += s.top();
                        s.pop();
                    }
                    s.push(input[i]);
                    break;
                case ')':
                    while(!s.empty() && s.top()!='('){
                        res+=s.top();
                        s.pop();
                    }
                    s.pop();
                    break;
            }
        }
        
    }
    while(!s.empty()){
        res += s.top();
        s.pop();
    }
    return res;
}

int main(){
    string input;
    cin >> input;
    
    printf("%s\n", solve(input).c_str());
    return 0;
}