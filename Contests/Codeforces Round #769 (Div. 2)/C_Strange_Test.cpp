#include <bits/stdc++.h>
using namespace std;

int solve(int a, int b, int cnt)
{
    if (a==b)
        return cnt;
    
    if (b>a)
    {
        if ((a|b)-b < b-a)
            return solve((a|b), b, cnt+1);
        else
            return solve(a+1, b, cnt+1);
    }    
    else
        return cnt + a-b;
}

signed main()
{
    // ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

    int tt, a, b, c, m, n, l, r, t, x, y, z, ans, sum, min_ans;
    
    cin >> tt;
    
    while (tt--)
    {
        
        cin>>a>>b;
        min_ans = b-a;

        for (int b1=b; b1<=(a|b); ++b1)
        {
            ans = solve(a, b1, 0) + b1-b;
            if (ans<min_ans)
                min_ans = ans;
        }

        printf("%d\n", min_ans);

    }
    
    return 0;
}