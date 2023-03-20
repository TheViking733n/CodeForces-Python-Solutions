#include <bits/stdc++.h>

using namespace std;

signed main()
{
    int TestCases=1;
    
    cin >> TestCases;
    
    while (TestCases--)
    {
        int n=0;
        cin >> n;
        
        vector<int> a(n);
        for (int i=0; i<n; i++) cin >> a[i];

        vector<int> b(n);
        for (int i=0; i<n; i++) cin >> b[i];

        bool yes=1;
        int mindiff = b[0] - a[0];

        for (int i=0; i<n; i++) {
            mindiff = min(mindiff, b[i] - a[i]);
        }
        
        // cout << mindiff << endl;

        if (mindiff < 0) {
            cout << "NO" << endl;
            continue;
        }
        int ind = 0;
        for (int i=0; i<n; i++) {
            a[i] += mindiff;
            if (a[i] == b[i]) ind = i;
        }



        
        for (int i=1; i<n; i++) {
            int ii = (ind - i) % n;
            a[ii] = min(a[(ii+1)%n] + 1, b[ii]);
        }

        for (int i=0; i<n; i++) {
            if (a[i] != b[i]) {
                yes = 0;
                break;
            }
        }
        
        
        cout << (yes ? "YES" : "NO") << endl;

        // if (yes) {
        //     cout << "YES" << endl;
        // } else {
        //     cout << "NO" << endl;
        // }

        
        
        
        
        
        
        
    }
    
    return 0;
}