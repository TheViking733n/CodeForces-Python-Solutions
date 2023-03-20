#include <iostream>

using namespace std;

int main()
{
    int a, b, c, n, t, max, left;

    cin >> t;

    while (t--)
    {
        cin>>a>>b>>c>>n;
        max = a>b&&a>c?a:b>c?b:c;
        left = n + a + b + c - 3*max;
        if (!(left%3) && left>=0)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }

    return 0;
}