#include <bits/stdc++.h>

using namespace std;

int main()
{
    string num, ans;
    int t, d1, d2, sum, ind, len;
    cin >> t;
    
    while (t--)
    {
        cin>>num;
        ans = "";
        sum = -1; ind = -1;
        len = num.size();
        for (int i = len-1; i > 0; --i)
        {
            d1 = num[i-1] - 48;
            d2 = num[i] - 48;
            if (d1+d2>9)
            {
                sum = d1+d2;
                ind = i-1;
                break;
            }
        }
        if (ind == -1)
        {

            d1 = num[0] - 48;
            d2 = num[1] - 48;
            sum = d1+d2;
            cout<<sum<<(num.substr(2))<<"\n";
        }
        else
        {
            cout<<(num.substr(0, ind));
            cout<<sum;
            cout<<(num.substr(ind+2))<<"\n";
        }

        

    }

    return 0;
}