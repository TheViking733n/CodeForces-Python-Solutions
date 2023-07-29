#pragma region
#pragma GCC optimize("Ofast")
// #pragma GCC optimize("unroll-loops")
// #define _CRT_SECURE_NO_WARNINGS
#include <bits/stdc++.h>
// #include <ext/pb_ds/assoc_container.hpp>
// #include <ext/pb_ds/trie_policy.hpp>

using namespace std;
// using namespace __gnu_pbds;

// ================================== Template Begins ==================================

#define int long long int   // DISABLE THIS IF MEMORY LIMIT EXCEEDS
#define FAST ios_base::sync_with_stdio(false);cin.tie(NULL);

#define ll long long
#define ld long double
#define mp make_pair
#define pb push_back
#define ss second
#define ff first
#define lb lower_bound
#define ub upper_bound
#define endl "\n"
#define sz(x) ((int)x.size())
#define all(v) (v).begin(), (v).end()
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define itt vector<int>:: iterator
#define fr(i, a, b) for(int i = (a); i < (b); ++i)
#define fb(i, b, a) for(int i = (b); i > (a); --i)
#define fill(x,y) memset(x,y,sizeof(x))

typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
typedef vector<string>  vs;

const int mod = 1000*1000*1000+7;
// const long long mod = 998244353;
const long double PI = 3.14159265358979323846264338;
//const double PI=acosl(-1);
const int inf = 1e18+5;

// Operator overloads <<, >>
template<typename T1, typename T2> // cin >> pair
istream &operator>>(istream &istream, pair<T1, T2> &p) { return (istream >> p.first >> p.second); }
template<typename T> // cin >> vector
istream &operator>>(istream &istream, vector<T> &v) { for (auto &it : v) { cin >> it; } return istream; }
template<typename T1, typename T2> // cout << pair
ostream &operator<<(ostream &ostream, const pair<T1, T2> &p) { return (ostream << p.first << " " << p.second); }
template<typename T> // cout << vector
ostream &operator<<(ostream &ostream, const vector<T> &c) { for (auto &it : c) { cout << it << " "; } return ostream; }

// ================================== Template Ends ==================================

#define max3(a,b,c) max(max((a),(b)),(c))
#define max4(a,b,c,d) max(max((a),(b)),max((c),(d)))
#define min3(a,b,c) min(min((a),(b)),(c))
#define min4(a,b,c,d) min(min((a),(b)),min((c),(d)))

int gcd(int a , int b) {return __gcd(a, b);}
int lcm(int a , int b) {return (a / gcd(a, b)) * b;}

#define YES(CONDITION) cout << ((CONDITION) ? "YES" : "NO") << "\n";
#define Yes(CONDITION) cout << ((CONDITION) ? "Yes" : "No") << "\n";

int floor1(int n,int k){
    if(n%k == 0 || n >= 0)return n/k;
    return (n/k)-1;
}
 
int ceil1(int n,int k){
    return floor1(n+k-1,k);
}
 
int powm(int a, int b) {
    int res=1;
    while(b) {
        if(b&1)
            res=(res*a)%mod;
        a=(a*a)%mod;
        b>>=1;
    }
    return res;
}

bool isPrime(int n) {
    if (n <= 1)  return false;
       if (n <= 3)  return true;
       if (n%2 == 0 || n%3 == 0) return false;
       for (int i=5; i*i<=n; i=i+6)
           if (n%i == 0 || n%(i+2) == 0)
               return false;
       return true;
}

// ================================== Debug Starts ==================================
// void __print(int x) {cerr << x;}
void __print(long x) {cerr << x;}
void __print(long long x) {cerr << x;}
void __print(unsigned x) {cerr << x;}
void __print(unsigned long x) {cerr << x;}
void __print(unsigned long long x) {cerr << x;}
void __print(float x) {cerr << x;}
void __print(double x) {cerr << x;}
void __print(long double x) {cerr << x;}
void __print(char x) {cerr << '\'' << x << '\'';}
void __print(const char *x) {cerr << '\"' << x << '\"';}
void __print(const string &x) {cerr << '\"' << x << '\"';}
void __print(bool x) {cerr << (x ? "true" : "false");}

template<typename T, typename V>
void __print(const pair<T, V> &x) {cerr << '{'; __print(x.first); cerr << ','; __print(x.second); cerr << '}';}
template<typename T>
void __print(const T &x) {int f = 0; cerr << '{'; for (auto &i: x) cerr << (f++ ? "," : ""), __print(i); cerr << "}";}
void _print() {cerr << "]\n";}
template <typename T, typename... V>
void _print(T t, V... v) {__print(t); if (sizeof...(v)) cerr << ", "; _print(v...);}
#ifndef ONLINE_JUDGE
#define debug(x...) cerr << "[" << #x << "] = ["; _print(x)
#else
#define debug(x...)
#endif
// ================================== Debug Ends ==================================
#pragma endregion


int N=1e6+5;
vector<int>tree[5*N];
int A[N];
Void build_tree( int cur , int l , int r )
{
     if( l==r )
     {
            tree[cur].push_back( a[ l ] );
            return ;
     }
     int mid = l+(r-l)/2;
     build_tree(2*cur+1 , l , mid ); // Build left tree 
     build_tree(2*cur+2 , mid+1 , r ); // Build right tree
     tree[cur] = merge( tree[2*cur+1] , tree[2*cur+2] ); //Merging the two sorted arrays
}

int query( int cur, int l, int r, int x, int y, int k)
{
       if( r < x || l > y )
      {
               return 0; //out of range
      }
      if( x<=l && r<=y )
      {
              //Binary search over the current sorted vector to find elements smaller than K

              Return lower_bound(tree[cur].begin(),tree[cur].end(),K)-tree[cur].begin();
      }
      int mid=l+(r-l)/2;
     return query(2*cur+1,l,mid,x,y,k)+query(2*cur+2,mid+1,r,x,y,k);
}


const int MOD=1e9+7,llmx=1e17,MX = 4e6+100,MN=4e6+100;
int tmx[MX],tmn[MN];
void build(int a[],int tl, int tr,int v) {
    if (tl == tr) {
        tmx[v] = a[tl];
    } else {
        int tm = (tl + tr)>>1;
        build(a, tl, tm,2*v+1);
        build(a, tm+1, tr,2*v+2);
        tmx[v] = max(tmx[v*2+1] ,tmx[v*2+2]);
    }
}
int Query(int tl,int tr,int l,int r,int nd) {
    if(tl>r || tr<l){return -llmx;}
    if(tr<=r && tl>=l){return tmx[nd];}
    int md = (tl+tr)>>1;
    int lfn=Query(tl,md,l,r,2*nd+1);
    int rgn=Query(md+1,tr,l,r,2*nd+2);
    return max(lfn,rgn);
}
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        tmx[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2+1, tl, tm, pos, new_val);
        else
            update(v*2+2, tm+1, tr, pos, new_val);
        tmx[v] = max(tmx[v*2+1],tmx[v*2+2]);
    }
}
void build1(int a[],int tl, int tr,int v) {
    if (tl == tr) {
        tmn[v] = a[tl];
    } else {
        int tm = (tl + tr)>>1;
        build1(a, tl, tm,2*v+1);
        build1(a, tm+1, tr,2*v+2);
        tmn[v] = min(tmn[v*2+1] ,tmn[v*2+2]);
    }
}
int Query1(int tl,int tr,int l,int r,int nd) {
    if(tl>r || tr<l){return llmx;}
    if(tr<=r && tl>=l){return tmn[nd];}
    int md = (tl+tr)>>1;
    int lfn=Query1(tl,md,l,r,2*nd+1);
    int rgn=Query1(md+1,tr,l,r,2*nd+2);
    return min(lfn,rgn);
}
void update1(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        tmn[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update1(v*2+1, tl, tm, pos, new_val);
        else
            update1(v*2+2, tm+1, tr, pos, new_val);
        tmn[v] = min(tmn[v*2+1],tmn[v*2+2]);
    }
}

int encode(x, y) {
    return x << 20 | y;
}
pii decode(z) {
    return {z >> 20, z & (1 << 20) - 1};
}

int f(int st, int en) {
    if (st >= en) return 0;
    auto [mn, idx1] = decode(Query1(0, n - 1, st, en - 1, 0));
    auto [mx, idx2] = decode(Query(0, n - 1, st, en - 1, 0));
    int ans = 0;
    if (idx1 < idx2) {
        ans += idx2 - idx1 + 1 - query(0, idx1, idx2, 0, n-1, mn);
        ans += query(0, idx2, en - 1, 0, n-1, mx);
        int left = idx1 - st + 1;
        int right = en - idx2 + 1;
        ans += left * right;
    }

}

signed main()
{
    FAST
    
    int TestCases=1, a, b, c, k, m, n, l, r, t, x, y, z, ans, sum;
    
    
    while (TestCases--)
    {
        cin >> n;
        
        vi arr(n);
        cin >> arr;
        for (int i = 0; i < n; i++) arr[i]--;

        vi a2(n);
        for (int i = 0; i < n; i++) a2[i] = encode(arr[i], i);


        
        
        
        
        
        
        
        
        
    }
    
    return 0;
}