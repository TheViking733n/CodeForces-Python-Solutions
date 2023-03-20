#include <bits/stdc++.h>
using namespace std;
#define gc getchar_unlocked
#define fo(i,n) for(i=0;i<n;i++)
#define Fo(i,k,n) for(i=k;i<n;i++)
#define ll long long
#define si(x)			scanf("%d",&x)
#define si2(x, y)	    scanf("%d%d",&x, &y)
#define si3(x, y, z)		scanf("%d%d%d",&x, &y, &z)
#define si4(x, y, z, w)	scanf("%d%d%d%d",&x, &y, &z, &w)
#define sll(x)			scanf("%I64d",&x)
#define sll2(x, y)	    scanf("%I64d%I64d",&x, &y)
#define sll3(x, y, z)	scanf("%I64d%I64d%I64d",&x, &y, &z)
#define sll4(x, y, z, w)	scanf("%I64d%I64d%I64d%I64d",&x, &y, &z, &w)
#define ss(s)			scanf("%s",s)
#define pi(x)			printf("%d\n",x)
#define pi2(x, y)		printf("%d %d\n",x,y)
#define pi3(x, y, z)		printf("%d %d %d\n",x,y,z)
#define pi4(x, y, z, w)	printf("%d %d %d %d\n",x,y,z,w)
#define pll(x)	printf("%lld\n",x)
#define ps(s)	printf("%s\n",s)
#define max3(x, y, z)	max(max(x, y), z)
#define max4(x, y, z, w)	max(max(x, y), max(z, w)
#define min3(x, y, z)	min(min(x, y), z)
#define min4(x, y, z, w)	min(min(x, y), min(z, w)
#define deb(x) cout << #x << " = " << x << endl
#define deb2(x, y) cout << #x << " = " << x << " , " << #y << " = " << y << endl
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define clr(x) memset(x, 0, sizeof(x))
#define tr(it, a) for(auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
typedef pair<int, int>	pii;
typedef pair<ll, ll>	pll;
typedef vector<int>		vi;
typedef vector<ll>		vl;
typedef vector<pii>		vpii;
typedef vector<pll>		vpll;
typedef vector<vi>		vvi;
typedef vector<vl>		vvl;
const int mod = 1000000007;
//================================================



signed main()
{
    // ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
    
    vi arr;
    int TestCases=1, a, b, c, k, m, n, l, r, t, x, y, z, ans, sum;
    string s, rev;
    cin >> TestCases;
    
    while (TestCases--)
    {
        arr = {};
        rev = "";
        cin>>n>>k>>s;

        for(int i=s.length()-1; i>=0; i--)
            rev = rev + s[i];  

        if (rev==s || k==0)
        {
            printf("1\n");
        }
        else
        {
            printf("2\n");
        }

        
    



        
        
    }
    
    return 0;
}