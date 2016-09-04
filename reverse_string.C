#include<iostream>
#include<stdlib.h>

using namespace std;

int main()
{
	string str;
//	string str2="sdjklfjsd";
	cin >> str;
//	cout << str.length();
	int len = str.length();
	for (int i=0; i<len/2;i++){
		char tmp;
		tmp = str[i];
		str[i] = str[len-1-i];
		str[len-1-i] = tmp;
		//tmp = str[i];
		//cout << tmp << endl;
	}
//	system("pause");
	cout << str;
	return 0;
}
