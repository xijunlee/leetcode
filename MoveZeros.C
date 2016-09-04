/*************************************************************************
    > File Name: MoveZeros.C
    > Author: 
    > Mail: 
    > Created Time: 二  7/ 5 10:06:52 2016
 ************************************************************************/

#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int n,tmp;
    cin >> n;
    vector<int> v;
    vector<int>::iterator iter;
    int size;    
    for (int i=0;i<n;i++){
        cin>>tmp;
        v.push_back(tmp);
    }
    size = v.size();
    int i=0;
    for (iter=v.begin();i<size;iter++,i++){
        if (*iter == 0){
           v.erase(iter);
           v.push_back(0);
        }
    }
        for (iter=v.begin();iter!=v.end();iter++){
            cout << *iter << " ";
        }
    return 0;
}
