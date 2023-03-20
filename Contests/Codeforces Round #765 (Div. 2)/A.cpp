#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, x, l, y, slider, cnt0, cnt1;
    vector <int> arr;
    cin >> t;
    while (t--)
    {
        slider = 1;
        y = 0;
        arr = {};
        cin>>n>>l;
        
        for (int i=0; i<n ; ++i)
        {
            cin>>x;
            arr.push_back(x);
        }

        for (int pos=0; pos<l ; ++pos)
        {
            cnt0 = 0; cnt1 = 0;
            for (int i=0; i<n ; ++i)
            {
                if(arr[i]&1)
                    ++cnt1;
                else
                    ++cnt0;
                arr[i] = arr[i]>>1;
            }
            if(cnt1>cnt0)
                y = y|slider;
            slider = slider<<1;
        }
        cout<<y<<"\n";

    }

    return 0;
}