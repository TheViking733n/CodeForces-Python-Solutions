/*
     ॐ त्र्यम्बकं यजामहे सुगन्धिं पुष्टिवर्धनम् |
     उर्वारुकमिव बन्धनान्मृत्योर्मुक्षीय माऽमृतात् ||
*/

#include <bits/stdc++.h>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>

using namespace std;
using namespace __gnu_pbds;

typedef tree<int, null_type, less<int>, rb_tree_tag, tree_order_statistics_node_update> pbds; // *arr.find_by_order(index), arr.order_of_key(num)

#define int long long int
#define double long double

#define find_bo find_by_order
#define rank order_of_key

#define F first
#define S second
#define pb push_back
#define mp make_pair

#define mt make_tuple
#define eb emplace_back

#define ub upper_bound
#define lb lower_bound
#define bs binary_search

#define min3(a, b, c) min(a, min(b, c))
#define min4(a, b, c, d) min(a, min(b, min(c, d)))
#define max3(a, b, c) max(a, max(b, c))
#define max4(a, b, c, d) max(max(a, b), max(c, d))

#define si set<int>
#define usi unordered_set<int>
#define vi vector<int>
#define vd vector<double>
#define umi unordered_map<int, int>

#define input(x) \
    int n;       \
    cin >> x;

#define pii pair<int, int>
#define vpi vector<pii>
#define vpp vector<pair<int, pii>>
#define mii map<int, int>
#define mpi map<pii, int>
#define spi set<pii>
#define endl "\n"

#define sz(x) ((int)x.size())
#define all(p) p.begin(), p.end()

#define pq_max priority_queue<int>
#define pq_min priority_queue<int, vi, greater<int>>

#define bug(...) __f(#__VA_ARGS__, __VA_ARGS__)

#define show(x)           \
    for (auto y : x)      \
        cout << y << " "; \
    cout << endl

#define showvp(a)    \
    for (auto x : a) \
    cout << x.F << " " << x.S << endl

#define take(x)       \
    for (auto &y : x) \
    cin >> y

#define YES cout << "YES" << endl;
#define NO cout << "NO" << endl;

inline int power(int a, int b)
{
    int x = 1;
    while (b)
    {
        if (b & 1)
            x *= a;
        a *= a;
        b >>= 1;
    }
    return x;
}

vector<int> sieve(int n)
{
    int *arr = new int[n + 1]();
    vector<int> vect;
    for (int i = 2; i <= n; i++)
        if (arr[i] == 0)
        {
            vect.push_back(i);
            for (int j = 2 * i; j <= n; j += i)
                arr[j] = 1;
        }
    return vect;
}

int maxarr(vi arr)
{
    int ans = arr[0];
    for (auto x : arr)
    {
        ans = max(ans, x);
    }
    return ans;
}

int minarr(vi arr)
{
    int ans = arr[0];
    for (auto x : arr)
    {
        ans = min(ans, x);
    }
    return ans;
}

int sumarr(vi arr)
{
    int ans{};
    for (auto x : arr)
    {
        ans += x;
    }
    return ans;
}

// printing [nth,(n+1)th] fibonacci number.  //a = fib(n).first
pair<int, int> fib(int n)
{
    if (n == 0)
        return {0, 1};

    auto p = fib(n >> 1);
    int c = p.first * (2 * p.second - p.first);
    int d = p.first * p.first + p.second * p.second;
    if (n & 1)
        return {d, c + d};
    else
        return {c, d};
}

void print() { cout << endl; }
template <typename T, typename... Types>
void print(T var1, Types... var2)
{
    cout << var1 << " ";
    print(var2...);
}

template <typename Arg1>
void __f(const char *name, Arg1 &&arg1) { cout << name << " : " << arg1 << endl; }
template <typename Arg1, typename... Args>
void __f(const char *names, Arg1 &&arg1, Args &&...args)
{
    const char *comma = strchr(names + 1, ',');
    cout.write(names, comma - names) << " : " << arg1 << " | ";
    __f(comma + 1, args...);
}

const int N = 200005;

int calc(vi a, int size)
{
    int max_so_far = INT_MIN, max_ending_here = 0;

    for (int i = 0; i < size; i++)
    {
        max_ending_here = max_ending_here + a[i];
        if (max_so_far < max_ending_here)
            max_so_far = max_ending_here;

        if (max_ending_here < 0)
            max_ending_here = 0;
    }
    return max_so_far;
}

usi factors(int n)
{
    usi s;
    for (int i = 1; i <= sqrt(n); i++)
    {
        if (n % i == 0)
        {
            if (n / i == i)
                s.insert(i);
            else
            {
                s.insert(i);
                s.insert(n / i);
            }
        }
    }
    return s;
}

void solve()
{
    int n;
    cin >> n;

    usi s;
    for (int i = 0; i < n; i++)
    {
        int a,b;
        cin >> a >> b;

        usi temp = factors(n);
        for (auto &&i : temp)
        {
            s.insert(i*b);
        }
    }
    print(s.size());
}

int32_t main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif

    clock_t z = clock();

    int t{1};
    cin >> t;
    while (t--)
        solve();

    cerr << "Run Time : " << ((double)(clock() - z) / CLOCKS_PER_SEC);

    return 0;
}