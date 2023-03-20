#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> arr;
    int n, t=1, x, sum, ans, left;

    // cin>>t;

    while (t--)
    {
        arr = {};
        sum = 0;
        cin>>n;
        
        for (int i = 0; i < 7; i++)
        {
            cin>>x;
            arr.push_back(x);
            sum += x;
        }

        if (sum == 1)
        {
            for (int i = 0; i < 7; i++)
            {
                if (arr[i] == 1)
                {
                    ans = i+1;
                    break;
                }
            }
            cout<<ans<<"\n";
            continue;
        }

        left = n%sum;

        if (left == 0)
        {
            ans = 7;
            for (int i = 6; i >=0 ; i--)
            {
                if (arr[i] == 0)
                {
                    ans--;
                }
                else break;
            }

            cout<<ans<<"\n";
            continue;
        }

        ans = 0;
        while (left > 0)
        {
            left -= arr[ans];
            ans++;
        }

        cout<<ans<<"\n";
    
    }
    
    
    return 0;
}