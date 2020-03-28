#include <vector>
#include <string>
#include <iostream>

using namespace std;

int main(){

	vector<string> s;
	int cnt = 0;
	s.push_back(to_string(cnt) + "hello");
	cout << s[0] << endl;
	return 0;
}
