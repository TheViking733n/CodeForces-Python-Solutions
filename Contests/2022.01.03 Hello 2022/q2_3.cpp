#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int t, n, l, r, c, lower, higher, a, b, lp, hp, abp, ans;
    // lower is the lowest and cheapest number among all l, and lp is price of lower
    // higher is the highest and cheapest number among all r, and hp is price of higher
    // a and b is the set containing maximum number of elements, and abp is its price

    cin >> t;
    while (t--)
    {
        cin>>n>>l>>r>>c;
        lower = l;
        higher = r;
        a = l; b = r;
        lp = c; hp = c; abp = c;

        cout<<c<<"\n";

        for(int i=1 ; i<n ; ++i)
        {
            cin>>l>>r>>c;
            
            if (lower > l)
            {
                lower = l;
                lp = c;

            }
            else if (lower == l && lp>c)
            {
                lower = l;
                lp = c;
            }

            if (higher < r)
            {
                higher = r;
                hp = c;
            }
            else if (higher == r && hp>c)
            {
                higher = r;
                hp = c;
            }

            if(b-a < r-l)
            {
                a = l;
                b = r;
                abp = c;
            }
            else if(b-a == r-l && abp>c)
            {
                a = l;
                b = r;
                abp = c;
            }
            // printf("\n%d %d %d %d\n", lower, higher, a, b);
            if(lower == a && higher == b)
            {
                ans = min(lp+hp, abp);
            }
            else
            {
                ans = lp+hp;
            }
            cout<<ans<<"\n";
        }

    }
    return 0;
}