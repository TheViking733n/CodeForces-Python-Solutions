/**
Remove Smallest

You are given the array a consisting of n positive (greater than zero) integers.

*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, x;
    cin>>t;

    while(t--)
    {
        string ans = "YES\n";
        vector<int> numbers;
        cin>>n;

        for(int i=0 ; i<n ; ++i)
        {
            cin>>x;
            numbers.push_back(x);
        }

        sort(numbers.begin(), numbers.end());

        for(int i=0 ; i<n-1 ; ++i)
        {
            if(numbers[i+1]-numbers[i] > 1)
            {
                ans = "NO\n";
                break;
            }
        }
        
        cout<<ans;
    }

    return 0;
}


        
