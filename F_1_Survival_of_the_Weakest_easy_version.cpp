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

const int M = 1000*1000*1000+7;
const int mod = 1000*1000*1000+7;
// const long long mod = 998244353;
const long double PI = 3.14159265358979323846264338;
//const double PI=acosl(-1);
// const int inf = 1e18+5;

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



signed main()
{
    FAST
    
    int TestCases=1, a, b, c, k, m, n, l, r, t, x, y, z, ans, sum;
    
    // cin >> TestCases;
    
    while (TestCases--)
    {
        cin >> n;
        
        vi arr(n);
        cin >> arr;
        vi excess;
        vi newarr;
        
        while (n > 1) {
            sort(all(arr));
            excess.push_back(arr[0]);
            for (int i=0; i<n; i++) arr[n-1-i] -= arr[0];
            priority_queue<pair<int, pii>> pq;

            for (int i=0; i<n-1; i++) {
                // vi temp{arr[i] + arr[i+1], i, i+1};
                pair<int, pii> temp = {arr[i] + arr[i+1], mp(i, i+1)};
                pq.push(temp);
            }
            newarr.clear();

            for (int i=0; i<n-1; i++) {
                pair<int, pii> cur = pq.top();
                pq.pop();
                newarr.pb(cur.first);
                if (cur.ss.ss < n) {
                    // vi temp{arr[cur[1]] + arr[cur[2]+1], arr[cur[1]], arr[cur[1]]+1};
                    pair<int, pii> temp = {arr[cur.ss.ff] + arr[cur.ss.ss+1], mp(cur.ss.ff, cur.ss.ss+1)};
                    pq.push(temp);
                }
            }
            arr = newarr;
            cout << arr << endl;
            n--;
        }

        int ans = arr[0];
        cout << excess << endl;
        reverse(all(excess));
        int v = 2;
        for (auto i : excess) {
            ans += i * v;
            ans %= M;
            v <<= 1;
            while (v > M) v -= M;
        }
        cout << ans << endl;
        
        
        
        
        
        
        
        
        
    }
    
    return 0;
}