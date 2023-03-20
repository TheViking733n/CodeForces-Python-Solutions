/**
Is your horseshoe on the other hoof?

Valera the Horse is going to the party with friends.
He has been following the fashion trends for a while,
and he knows that it is very popular to wear all horseshoes of different color.
Valera has got four horseshoes left from the last year, but maybe some of them have the same color.
In this case he needs to go to the store and buy some few more horseshoes,
not to lose face in front of his stylish comrades.

 */



#include <bits/stdc++.h>

using namespace std;

int main()
{   
    int n, c=0;
    vector<int> arr;
    
    cin>>n; arr.push_back(n);
    cin>>n; arr.push_back(n);
    cin>>n; arr.push_back(n);
    cin>>n; arr.push_back(n);

    sort(arr.begin(), arr.end());

    if (arr[0]==arr[1]) c++;
    if (arr[1]==arr[2]) c++;
    if (arr[2]==arr[3]) c++;
    
    cout<<c;

    return 0;
}
