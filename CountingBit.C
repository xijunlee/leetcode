/*************************************************************************
	> File Name: CountingBit.C
	> Author: 
	> Mail: 
	> Created Time: 一  7/ 4 22:49:56 2016
 ************************************************************************/

#include<stdio.h>
#include<iostream>

using namespace std;

int main()
{
    int n,tmp,count;
    cin >> n;
    for (int i=0;i<n;i++){
        tmp = i;
        count = 0;
        while (tmp>0){
         if (tmp%2==1)
            count++;
         tmp /= 2;
        }
    }
    return 0;
}
