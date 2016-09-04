#include <iostream>
#include <stdlib.h>

using namespace std;
int main()
{
	int a=0,b=0;
	cin>>a>>b;
	a=a^b;
	b=a^b;
	a=a^b;



	cout<<a<<b;
}
