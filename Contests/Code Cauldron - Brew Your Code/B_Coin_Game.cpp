#include <bits/stdc++.h>
 
#define pii              pair <int,int>
#define pll              pair <long long,long long>
#define sc               scanf
#define pf               printf
#define Pi               2*acos(0.0)
#define ms(a,b)          memset(a, b, sizeof(a))
#define pb(a)            push_back(a)
#define MP               make_pair
#define db               double
#define ll               long long
#define EPS              10E-10
#define ff               first
#define ss               second
#define sqr(x)           (x)*(x)
#define D(x)             cout<<#x &quot; = &quot;<<(x)<<endl
#define VI               vector <int>
#define DBG              pf(&quot;Hi\n&quot;)
#define MOD              1000000007
#define CIN              ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
#define SZ(a)            (int)a.size()
#define sf(a)            scanf(&quot;%d&quot;,&a)
#define sfl(a)           scanf(&quot;%lld&quot;,&a)
#define sff(a,b)         scanf(&quot;%d %d&quot;,&a,&b)
#define sffl(a,b)        scanf(&quot;%lld %lld&quot;,&a,&b)
#define sfff(a,b,c)      scanf(&quot;%d %d %d&quot;,&a,&b,&c)
#define sfffl(a,b,c)     scanf(&quot;%lld %lld %lld&quot;,&a,&b,&c)
#define stlloop(v)       for(__typeof(v.begin()) it=v.begin();it!=v.end();it++)
#define loop(i,n)        for(int i=0;i<n;i++)
#define loop1(i,n)       for(int i=1;i<=n;i++)
#define REP(i,a,b)       for(int i=a;i<b;i++)
#define RREP(i,a,b)      for(int i=a;i>=b;i--)
#define TEST_CASE(t)     for(int z=1;z<=t;z++)
#define PRINT_CASE       printf(&quot;Case %d: &quot;,z)
#define LINE_PRINT_CASE  printf(&quot;Case %d:\n&quot;,z)
#define CASE_PRINT       cout<<&quot;Case &quot;<<z<<&quot;: &quot;
#define all(a)           a.begin(),a.end()
#define intlim           2147483648
#define infinity         (1<<28)
#define ull              unsigned long long
#define gcd(a, b)        __gcd(a, b)
#define lcm(a, b)        ((a)*((b)/gcd(a,b)))
 
using namespace std;
 
 
//----------------------Graph Moves----------------
//const int fx[]={+1,-1,+0,+0};
//const int fy[]={+0,+0,+1,-1};
//const int fx[]={+0,+0,+1,-1,-1,+1,-1,+1};   // Kings Move
//const int fy[]={-1,+1,+0,+0,+1,+1,-1,-1};  // Kings Move
//const int fx[]={-2, -2, -1, -1,  1,  1,  2,  2};  // Knights Move
//const int fy[]={-1,  1, -2,  2, -2,  2, -1,  1}; // Knights Move
//------------------------------------------------
 
//-----------------------Bitmask------------------
//int Set(int N,int pos){return N=N | (1<<pos);}
//int reset(int N,int pos){return N= N & ~(1<<pos);}
//bool check(int N,int pos){return (bool)(N & (1<<pos));}
//------------------------------------------------
 
#define mx 2000006
 
bitset<mx/2>vis;
vector<int>prime;
 
vector<pii>factor;
 
void sieve()
{
    int x=mx/2,y=sqrt(mx)/2;
    for(int i=1; i<=y; i++)
    {
        if(vis[i]==0)
        {
            for(int j=i*(i+1)*2; j<x; j+=(2*i)+1)
                vis[j]=1;
        }
    }
 
    prime.pb(2);
 
    for(int i=3; i<mx; i+=2)
        if(vis[i/2]==0)
            prime.pb(i);
 
}
 
ll factorial[mx];
ll arr[mx];
 
 
vector<ll>ans;
 
void precal(ll p, ll q, ll mod)
{
    arr[0]=1;
    arr[1]=1;
//    ll mod=bigmod(p,q,MOD);
    ll x=1;
    for(ll i=2; i<=mod; i++)
    {
        if(i%p)
            x=i;
        else
            x=1;
        arr[i]=(arr[i-1]*x)%mod;
    }
}
 
ll bigmod(ll n, ll p, ll mod)
{
    ll ret=1;
    while(p)
    {
        if(p%2)
            ret=(ret*n)%mod;
        n=(n*n)%mod;
        p/=2;
    }
    return ret;
}
 
ll E(ll n, ll p)
{
    ll ret=0;
    while(n)
    {
        ret+=n/p;
        n=n/p;
    }
    return ret;
}
 
ll f(ll n, ll mod)
{
    ll ret=bigmod(arr[mod-1],n/mod,mod)*arr[n%mod];
    return ret;
}
 
ll F(ll n, ll mod, ll p)
{
    ll ret=1;
    ll i=1;
    while(i<=n)
    {
        ret=(ret*f(n/i,mod))%mod;
        i=i*p;
    }
    return ret;
}
 
int inv(int a, int m) // Calculating Modular Multiplicative Inverse
{
    int m0 = m, t, q;
    int x0 = 0, x1 = 1;
 
    if (m == 1)
        return 0;
 
//     Apply extended Euclid Algorithm
    while (a > 1)
    {
//         q is quotient
        q = a / m;
 
        t = m;
 
//         m is remainder now, process same as
//         euclid's algo
        m = a % m, a = t;
 
        t = x0;
 
        x0 = x1 - q * x0;
 
        x1 = t;
    }
 
//     Make x1 positive
    if (x1 < 0)
        x1 += m0;
 
    return x1;
}
 
 
 
 
ll nCr(ll n, ll r, ll p, ll mod)
{
    ll e=E(n,p)-E(r,p)-E(n-r,p);
    ll mod1=F(n,mod,p);
    ll mod2=(F(r,mod,p)*F(n-r,mod,p))%mod;
    mod2=inv(mod2,mod);
    ll ret=bigmod(p,e,mod);
    ret*=mod1;
    ret%=mod;
    ret*=mod2;
    ret%=mod;
    return ret;
}
 
ll findMinX(int k) // Chinese Remainder
{
    ll prod = 1;
    vector<int>num;
    for(int i=0; i<k; i++)
    {
        num.pb(bigmod(factor[i].ff,factor[i].ss,MOD));
    }
    for (int i = 0; i < k; i++)
        prod *= num[i];
 
    ll result = 0;
 
    for (int i = 0; i < k; i++)
    {
        ll pp = prod / num[i];
        result += ans[i] * inv(pp, num[i]) * pp;
    }
 
    return result % prod;
}
 
ll nCr_mod_m(ll n, ll r, ll m)
{
    factor.clear();
    ans.clear();
    int root=sqrt(m);
    ll mm=m;
    for(int i=0; i<SZ(prime) && prime[i]<=root; i++)
    {
        if(mm%prime[i]==0)
        {
            int cnt=0;
            while(mm%prime[i]==0)
            {
                mm/=prime[i];
                cnt++;
            }
            factor.pb(pii(prime[i],cnt));
            root=sqrt(mm);
        }
    }
 
    if(mm>1)
        factor.pb(pii(mm,1));
 
 
 
    for(int i=0; i<SZ(factor); i++)
    {
        ll p=factor[i].ff;
 
        ll num=bigmod(p,factor[i].ss,MOD);
        precal(p,factor[i].ss,num);
        ans.pb(nCr(n,r,p,num));
    }
 
    ll anss=findMinX(SZ(factor));
    return anss;
}
 
int main()
{
 
//    freopen(&quot;in.txt&quot;,&quot;r&quot;,stdin);
//    freopen(&quot;out.txt&quot;,&quot;w&quot;,stdout);
 
    sieve();
 
    int t=1;
    // cin >>t;
    while(t--)
    {
        ll n,r,m;
        cin>>n>>m;
        for (int r = 0; r<=n; r++) {
            ll ans=nCr_mod_m(n,r,m);
            cout << ans << " ";
        }
        cout << "\n";
 
    }
 
    return 0;
}