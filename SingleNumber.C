/*************************************************************************
	> File Name: SingleNumber.C
	> Author: 
	> Mail: 
	> Created Time: 一  7/ 4 13:08:59 2016
 ************************************************************************/

#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>

using namespace std;

int main()
{
   vector<int> v;
   for (int i=0;i<10;i++)
       v.push_back(i);
   for (int i=0;i<10;i++)
       v.push_back(i);
   for (int i=0;i<v.size();i++)
       cout<<v[i]<<endl;
   v.push_back(123);
   int res=v[0];
   for (int i=1;i<v.size();i++)
       res = res^v[i];
   cout << res << endl;
    return 0;
}
