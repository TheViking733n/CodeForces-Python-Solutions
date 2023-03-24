#include<bits/stdc++.h>
using namespace std;
#include<ext/pb_ds/assoc_container.hpp>
#include<ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define int long long
typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds;
void srtunq(vector<int> &v1){sort(v1.begin(),v1.end());v1.erase(unique(v1.begin(),v1.end()),v1.end());}
const int MOD=1e9+7;
const int MX = 1,MN=1;int tmx[MX],tmn[MN];
void build(int a[],int tl, int tr,int v) {
    if (tl == tr) {
        tmx[v] = a[tl];
    } else {
        int tm = (tl + tr)>>1;
        build(a, tl, tm,2*v+1);
        build(a, tm+1, tr,2*v+2);
        tmx[v] = tmx[v*2+1]^tmx[v*2+2];
    }
}
int Query(int tl,int tr,int l,int r,int nd) {
    if(tl>r || tr<l){return 0;}
    if(tr<=r && tl>=l){return tmx[nd];}
    int md = (tl+tr)>>1;
    int lfn=Query(tl,md,l,r,2*nd+1);
    int rgn=Query(md+1,tr,l,r,2*nd+2);
    return lfn^rgn;
}
void update(int v, int tl, int tr, int pos, int new_val) {
    if (tl == tr) {
        tmn[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2+1, tl, tm, pos, new_val);
        else
            update(v*2+2, tm+1, tr, pos, new_val);
        tmn[v] = tmn[v*2+1]^tmn[v*2+2];
    }
}
int power(int a, int b, int m) {
    a %= m;
    int res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}
int power1(int x, int y)
{
    int res = 1;
    while (y > 0) {
        if (y % 2 == 1)
            res = (res * x);
        y = y >> 1;
        x = (x * x);
    }
    return res;
}
int gcd(int a,int b)
{
if (b == 0)
    return a;
  return gcd(b, a % b);
}
int lcm(int a, int b)
{return (a / gcd(a, b)) * b;}
void SieveOfEratosthenes(int n)
{
    vector<int> v(1,-1);
    for(int i=2;i*i<=n;i++){
        if(v[i]==-1){
            for(int j=2;j*i<=n;j++){
                v[j*i]=i;
            }
        }
    }
}
int modInverse(int n, int p)
{
    return power(n, p - 2, p);
}
int nCrModPFermat(int n,int r, int p)
{
    if (n < r)
        return 0;
    if (r == 0)
        return 1;
    int fac[n + 1];
    fac[0] = 1;
    for (int i = 1; i <= n; i++)
        fac[i] = (fac[i - 1] * i) % p;
 
    return (fac[n] * modInverse(fac[r], p) % p
            * modInverse(fac[n - r], p) % p)
           % p;
}
vector<int> v1[1];
int dh[1],dp1[1][1];
void bldlft(int node,int parent,int dep){
    dh[node]=dep;
    if(parent!=0)dp1[node][0]=parent;
    for(int i=1;i<=20;i++){
        if(dp1[node][i-1]!=-1){
            dp1[node][i]=dp1[dp1[node][i-1]][i-1];
        }
    }
    for(int i=0;i<v1[node].size();i++){
        if(parent!=v1[node][i])
            bldlft(v1[node][i],node,dep+1);
    }
}
int fndlft(int a,int b){
        if(dh[a]>=dh[b]){
            int w = dh[a]-dh[b];
            while(w){
                int w1 = w&(-w);w-=w1;w1=log2(w1);
                a=dp1[a][w1];
            }
        }
        else {
            int w = dh[b]-dh[a];
            while(w){
                int w1 = w&(-w);w-=w1;w1=log2(w1);
                b=dp1[b][w1];
            }
        }
        if(a!=b){
            for(int j=20;j>=0;j--){if(dp1[a][j]!=dp1[b][j]){a=dp1[a][j];b=dp1[b][j];}}
            return dp1[a][0];}
        else{
            return a;
        }
}
map<int,int> mp;
vector<int> v[200001];
vector<pair<int,int>> odd,ev;
void dfs(int node,int parent,int depth){
    if(depth%2==0){ev.push_back({mp[node],node});}
    if(depth%2==1){odd.push_back({mp[node],node});}
    for(int i=0;i<v[node].size();i++){
        if(v[node][i]!=parent){
            dfs(v[node][i],node,depth+1);
        }
    }
}
void solve(){
     int n;cin>>n;
     mp.clear();odd.clear();ev.clear();
     for(int i=0;i<=n;i++)v[i].clear();
     int a[n];for(int i=0;i<n;i++){cin>>a[i];mp[i+1]=a[i];}
     for(int i=0;i<n-1;i++){
         int a,b;cin>>a>>b;v[a].push_back(b);v[b].push_back(a);
     }
     if(n==1){cout<<1<<"\n";return;}
     dfs(1,0,0);
    //  int x=0,y=0;
    //  pair<int,int> mn,mn1;
    //  mn.first=-1;
    // for(int i=0;i<odd.size();i++){
    //     y=y|odd[i].first;
    // }
    // for(int i=0;i<ev.size();i++){
    //     x=x^ev[i].first;
    // }
    vector<pair<int, int>> anss;
    for (int jj=0; jj < 2; jj++) {
        int anss1 = 0, anss2 = 0;
        for (auto i: ev) { anss1 ^= i.first;}
        for (auto i: odd) { anss2 |= i.first;}
        for (auto root: ev) {
            int a1 = anss1 ^ root.first;
            int a2 = anss2;
            anss.push_back({-a1-a2, root.second});
        }
        swap(ev, odd);
    }
    sort(anss.begin(), anss.end());
    // for (auto i: anss) {
    //     cout << i.second << " " << i.first << "\n";
    // }
    cout << anss[0].second << "\n";

    // for(int i=0;i<ev.size();i++){
    //     int temp=x^ev[i].first;
    //     if(temp>mn.first){
    //         mn.first=temp;mn.first=ev[i].second;
    //     }
    // }
    // cout<<mn.second<<"\n";return;
    // int x1 = 0,y1=0;
    // for(int i=0;i<odd.size();i++){
    //     x1=x1^odd[i];
    // }
    // for(int i=0;i<ev.size();i++){
    //     y1=y1|ev[i];
    // }
    // for(int i=0;i<odd.size();i++){
    //     int temp=x1^odd[i];
    //     mn=min(mn,temp+y);
    // }
    // cout<<mn<<"\n";
}
signed main(){
//#ifndef ONLINE_JUDGE
//freopen("./input.txt", "r", stdin);
//freopen("./output.txt", "w",stdout);
//#endif
ios_base::sync_with_stdio(false);
cin.tie(NULL);
int testcase=1;
   cin>>testcase;
   while(testcase--){
       solve();
   }
  return 0;
}