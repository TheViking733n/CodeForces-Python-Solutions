#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main() {
    int tt = 1;
    cin >> tt;

    while (tt--) {
        int n, m;
        cin >> n >> m;
        if (n > m) swap(n, m);
        int sz = n * m;
        vector<int> v(sz);
        for (int j = 0; j < sz; j++) cin >> v[j];
        
        sort(v.begin(), v.end());
        int ans1 = n * (m - 1) * (v[sz-1] - v[0]) + (n - 1) * (v[sz-1] - v[1]);
        reverse(v.begin(), v.end());
        int ans2 = n * (m - 1) * (v[sz-1] - v[0]) + (n - 1) * (v[sz-1] - v[1]);
        cout << max(ans1, -ans2) << endl;
    }
    return 0;
}
