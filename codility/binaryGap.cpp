// you can use includes, for example:
#include <stdio.h>
#include <iostream>
#include <algorithm>

using namespace std;
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(int N) {
    // write your code in C++14 (g++ 6.2.0)
    int res = 0; int tmp=0;
    cout << "input : " << N << endl;
    while(true){
       	if(N==0 || N==1)
		break;

	 if(N&1){
            // Found the first 1
            N = N>>1;tmp = 0;
            while( !(N&1)){
                tmp++;
                N = N>>1;
            }
	    if(N&1 && tmp > res){
		res = tmp;
	   }
        }else{
            N = N>>1;
        }
    }
    return res;
}

int main(){
	int output = solution(1);
	cout << "Output : " << output << endl;
	output = solution(2147483247);
	cout << "output: " << output << endl;
	output = solution(1041);
	cout << "Output : " << output << endl;
	return 0;
}
