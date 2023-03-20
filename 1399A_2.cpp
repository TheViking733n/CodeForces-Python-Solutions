/**
Remove Smallest

You are given the array a consisting of n positive (greater than zero) integers.

*/

#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, x, last_true_ind;
    cin>>t;

    while(t--)
    {
        last_true_ind = -1;
        string ans = "YES\n";
        vector<bool> numbers(100, false);
        cin>>n;

        for(int i=0 ; i<n ; ++i)
        {
            cin>>x;
            numbers[x-1] = true;
        }

        for(int i=0 ; i<n ; ++i)
        {
            if (numbers[i] == true)
            {
                if(last_true_ind == -1)
                {
                    last_true_ind = i;
                    continue;
                }
                else
                {
                    if(i-last_true_ind > 1)
                    {
                        ans = "NO\n";
                        break;
                    }
                    else
                    {
                        last_true_ind = i;
                    }
                }
            }
        }
        
        cout<<ans;
    }

    return 0;
}


        
