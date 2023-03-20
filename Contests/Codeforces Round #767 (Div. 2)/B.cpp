#include <bits/stdc++.h>
 
using namespace std;
 
int main()
{
 
    
    int t, l, r, k, n, x;
 
    cin>>t;
    while(t--)
    {
        cin>>l>>r>>k;
 
        n = r - l + 1;
 
        if (n==1)
            printf(((l==1)?"NO\n":"YES\n"));
        
        else
        {
 
            x = (n + l%2 + r%2 - 1)/2;
            printf(((x<=k)?"YES\n":"NO\n"));
 
 
        }
        
 
    }
 
    return 0;
}