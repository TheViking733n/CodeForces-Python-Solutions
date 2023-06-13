#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define int long long

int f(int i, int en, int pick, vector<pair<int, int>>& arr, vector<vector<int>>& dp) {
    if (dp[i][en] != -1) return dp[i][en];
    int n = arr.size();
    if (i >= n) return 0;
    int s = arr[i].first;
    int e = arr[i].second;
    if (pick) {
        if (s <= en) {
            dp[i][en] = 2 + f(i + 1, max(e, en), 1 - pick, arr, dp);
            return dp[i][en];
        }
        else {
            dp[i][en] = f(i + 1, max(e, en), pick, arr, dp);
            return dp[i][en];
        }
    }
    else {
        if (s >= en) { // Don't pick, en time of prev should be smaller than start of cur
            dp[i][en] = f(i + 1, max(e, en), 1 - pick, arr, dp);
            return dp[i][en];
        }
        else {
            dp[i][en] = f(i + 1, max(e, en), pick, arr, dp);
            return dp[i][en];
        }
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int TestCases = 1;
    cin >> TestCases;
    
    while (TestCases--) {
        int n;
        cin >> n;
        vector<pair<int, int>> arr(n);
        
        for (int i = 0; i < n; i++) {
            int u, v;
            cin >> u >> v;
            arr[i] = make_pair(u, v);
        }
        
        vector<int> a2;
        for (auto p : arr) {
            a2.push_back(p.first);
            a2.push_back(p.second);
        }
        sort(a2.begin(), a2.end());
        
        vector<int> a3;
        a3.push_back(a2[0]);
        for (int i = 1; i < a2.size(); i++) {
            if (a2[i] != a2[i - 1]) {
                a3.push_back(a2[i]);
            }
        }
        a2 = a3;
        int mx = *max_element(a2.begin(), a2.end()) + 1;
        
        vector<int> inv(mx);
        for (int i = 0; i < a2.size(); i++) {
            inv[a2[i]] = i;
        }
        for (int i = 0; i < n; i++) {
            arr[i] = make_pair(inv[arr[i].first], inv[arr[i].second]);
        }
        sort(arr.begin(), arr.end());
        
        vector<vector<int>> dp(n + 1, vector<int>(mx, -1));
        int ans = f(0, -1, 0, arr, dp);
        cout << n - ans << "\n";
    }
    
    return 0;
}
