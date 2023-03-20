#include <bits/stdc++.h>
using namespace std;

#define int long long int

signed main()
{
    int test;
    cin>>test;
    while(test--)
    {
        int n, x;
        cin>>n>>x;
        int a[n];
        for(int i=0; i<n; i++)
            cin>>a[i];
        
        sort(a, a+n);
        
        
        int sum=0;
        int pf[n];
        for(int i=0; i<n; i++)
        {
            sum+=a[i];
            pf[i]=sum;
        }
        
        int mx = pf[n-1];
        int day=0;
        

        
        
        int ans=0, i=n-1;;
        
        
        while(i >= 0)
        {
            if(pf[i] <= x-(day)*(i+1))
            {
                ans += i + 1;
                day++;
            } else
            i--;
        }
        
        
        cout<<ans<<"\n";
        
        
    }
    return 0;
}