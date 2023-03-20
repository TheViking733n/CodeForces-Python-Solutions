#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, a, b, c, a1, b1, c1;
    cin >> t;
    while (t--)
    {
        cin>>a>>b>>c;
        a1 = 2*b-c;
        b1 = (a+c)/2;
        c1 = 2*b-a;
        // printf("a1->%d  b1->%d  c1->%d\n", (a1%a == 0), (((a+c)%2==0 && b1%b==0)), (c1%c==0));
        if (
            (a1%a == 0 && a1>0) ||
            (c1%c == 0 && c1>0) ||
            ((a+c)%2==0 && b1>0 && b1%b==0)
                )
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }

    return 0;
}
