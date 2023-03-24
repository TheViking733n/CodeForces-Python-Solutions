#include<bits/stdc++.h>
using namespace std;
void actualcode();
#define ll long long int
#define ios ios_base::sync_with_stdio(false);cin.tie(NULL);
#define endl "\n"
#pragma GCC optimize("unroll-loops")
#pragma GCC optimize("Ofast")
#pragma GCC target("fma,sse,sse2,sse3,ssse3,sse4,popcnt,abm,mmx,avx,avx2,tune=native")
ll mod = 998244353;
typedef vector<int> vi;
typedef pair<int,int> pi;
typedef vector<ll> vl;
typedef pair<ll,ll> pl;
#define pb push_back
#define mp make_pair
ll max3(ll a, ll b, ll c){return(max(max(a,b),c));}
ll max4(ll a, ll b, ll c, ll d){return(max(max(max(a,b),c),d));}
ll gcd(ll a, ll b){return b == 0 ? a : gcd(b, a % b);}
void YES(){cout<<"yes"<<endl;}
void NO(){cout<<"no"<<endl;}
void yes(){cout<<"Yes"<<endl;}
void no(){cout<<"No"<<endl;}

int main()
{
    // #ifndef ONLINE_JUDGE
    //     freopen("1.txt","r",stdin);
    //     freopen("output8.txt","w",stdout);
    // #endif    
    actualcode();
}

ll pow(ll a, ll n)
{
    if(n==1)
    {
        return a;
    }
    else if(n==0)
    {
        return 1;
    }
    else if(n&1)
    {
        return (((pow(a,n/2)%mod)*(pow(a,n/2))%mod)*(a%mod)) ;
    }
    else
    {
        return ((pow(a,n/2)%mod)*(pow(a,n/2)%mod));
    }
    
}
 
void actualcode()
{
    int t=1;
    cin>>t;
    while(t--)
    {
        int n,k;
        cin>>n>>k;
        ll arr[n];
        for(int i=0;i<n;i++)
        {
            cin>>arr[i];
        }
        int freq[n];
        for(int i=0;i<n;i++)
        {
            freq[i]=0;
        }
        int tillnow=0;
        int kow=0;
        int wow=0;
        int ans=0;
        ll div;
        for(int i=1;i<n;i++)
        {
            if(i-k>=0)
            {
                kow+=freq[i-k];
            }
            div = pow(i+1,tillnow-kow);
            arr[i]/=div;
            if(i<n-k+1)
            {
                if(arr[i]>arr[i-1])
                {
                    wow=0;
                    while(arr[i]>arr[i-1])
                    {
                        arr[i]/=(i+1);
                        wow++;
                    }
                    ans+=wow;
                    tillnow+=wow;
                    freq[i]=wow;
                }
            }
            
        }
        wow=0;
        for(int i=n-1;i>=n-k+1;i--)
        {
            div = pow(i+1,wow);
            arr[i]/=div;
            if(arr[i]>arr[i-1])
            {
                while(arr[i]>arr[i-1])
                {
                    arr[i]/=(i+1);
                    arr[i-1]/=i;
                    wow++;
                }
            }
        }
        ans+=wow;
        cout<<ans<<endl;
    }
}