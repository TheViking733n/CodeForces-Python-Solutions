#include <bits/stdc++.h>
using namespace std;

typedef long long int lli;
typedef vector<lli> vll;
typedef vector<pair<lli, lli>> vpll;
typedef vector<bool> vb;

#define take(v)       \
    for (auto &x : v) \
    cin >> x
#define print(v)     \
    for (auto x : v) \
    cout << x << " "
#define printp(x)    \
    for (auto y : x) \
        cout << y.first << " " << y.second << "\n";

#define all(v) (v).begin(), (v).end
#define sz(x) ((lli)(x).size())
#define sort_asc(v) sort(all(v))
#define sort_des(v) sort(v.rbegin(), v.rend())
// map<char,lli> charval;
// for(lli i=97;i<=122;i++) charval.insert(mpr(char(i),i-96));

#define pll pair<lli, lli>
#define mpr(x, y) make_pair(x, y)
#define pb(x) push_back(x)
#define pob() pop_back()
#define eb emplace_back
#define F first
#define S second

#define fl(i, a, n) for (lli i = a; i < n; i++)
#define max4(a, b, c, d) max(max((a), (b)), max((c), (d)))
#define max3(a, b, c) max(max((a), (b)), (c))
#define min4(a, b, c, d) min(min((a), (b)), min((c), (d)))
#define min3(a, b, c) min(min((a), (b)), (c))

bool sortbysec(const pair<int, int> &a, const pair<int, int> &b)
{
    return (a.second < b.second);
}

void solve()
{
    lli n;
    cin >> n;
    vll v(n);
    vector<pair<lli, pll>> ans;
    map<lli, lli> fre;
    for (lli i = 0; i < n; i++)
    {
        cin >> v[i];
        fre[v[i]]++;
        if (fre[v[i]] == 1)
        {
            ans.pb(mpr(0, mpr(n - i, v[i])));
        }
    }
    for (lli i = 0; i < ans.size(); i++)
    {
        ans[i].F = fre[ans[i].S.S];
    }
    sort_des(ans);

    for (lli i = 0; i < ans.size(); i++)
    {
        cout << ans[i].S.S << " ";
    }
}
int main()
{
    int t = 1;
    // cin >> t;
    while (t--)
    {
        solve();
        // cout << "\n";
    }
    return 0;
}