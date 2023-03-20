// 2k-1 > n -> not stable

#include <iostream>

using namespace std;

int main()
{
    int t, n, k;
    cin >> t;
    while (t--)
    {
        cin>>n>>k;
        if (2*k-1 > n)
        {
            printf("-1\n");
        }
        else
        {
            for (int i=1 ; i<=n ; ++i)
            {
                for (int j=1 ; j<=n ; ++j)
                {
                    if (i==j && i%2 && j%2 && k>0)
                    {
                        cout<<"R";
                        --k;
                    }
                    else
                    {
                        cout<<".";
                    }
                }
                cout<<"\n";
            }
        }
    }
    return 0;
}   