#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, a, max, min;
    cin >> t;
    while (t--)
    {
        cin>>n>>a;
        max = a;
        min = a;
        for (int i = 1; i < n; ++i)
        {
            cin>>a;
            if(max<a)
            {
                max = a;
            }
            if (min>a)
            {
                min = a;
            }
        }
        cout<<(max-min)<<"\n";

    }

    return 0;
}