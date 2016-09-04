#include<iostream>
#include<stdlib.h>

using namespace std;

bool isHappy(int num)
{
	int hash[1000];
	for (int i=0;i<1000;i++)
	{
		hash[i] = 0;
	}
	bool shown = false;
	while(num!=1){
		int tmp = num;
		int sum = 0;
		while (tmp>0)
		{
			int tmp1 = tmp%10;
			sum += tmp1*tmp1;
			tmp /= 10;
		}
		num = sum;
		if (!hash[num])
			hash[num] = 1;
		else 
		{
			shown = true;
			break;
		}	
	}
	
	if (shown == false)
		return true;
	else
		return false;
	
};

int main(){
 	int n;
 	cin >> n;
 	cout << isHappy(n) << endl;
 	return 0;
}
