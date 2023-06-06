#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> solve(int n, vector<pair<int, int>>& edges, vector<int>& init) {
    vector<vector<int>> smaller(n);
    vector<int> ans = init;

    for (auto& edge : edges) {
        int sm = edge.first;
        int lar = edge.second;
        smaller[lar].push_back(sm);
        if (ans[lar] == -1) ans[lar] = 1;
        if (ans[sm] == -1) ans[sm] = 1;
    }

    for (int i = 0; i < n; i++) {
        if (init[i] != 0) continue;
        for (int u : smaller[i]) {
            ans[u] = init[u] = 1;
        }
    }

    for (int i = 0; i < n; i++) {
        if (!ans[i] || init[i] != -1) continue;
        bool zeroParFound = false;
        for (int sm : smaller[i]) {
            if (ans[sm] == 0) {
                zeroParFound = true;
                break;
            }
        }
        if (!zeroParFound) {
            ans[i] = 0;
        }
    }

    return ans;
}

int main() {
    int TestCases = 1;
    ios::sync_with_stdio(false);
    cin.tie(0);

    for (int _ = 0; _ < TestCases; _++) {
        int n, q;
        cin >> n >> q;
        vector<pair<int, int>> queries;
        vector<int> W;
        for (int i = 0; i < q; i++) {
            int u, v, w;
            cin >> u >> v >> w;
            u -= 1;
            v -= 1;
            queries.push_back({ min(u, v), max(u, v) });
            W.push_back(w);
        }
        vector<int> ans(n, 0);

        for (int bit = 0; bit < 30; bit++) {
            int mask = 1 << bit;
            vector<pair<int, int>> edges;
            vector<int> init(n, -1);
            for (int i = 0; i < q; i++) {
                int u = queries[i].first;
                int v = queries[i].second;
                int w = W[i];
                if (w & mask) {
                    if (u == v) init[u] = 1;
                    else edges.push_back({ u, v });
                }
                else {
                    init[u] = init[v] = 0;
                }
            }
            vector<int> curans = solve(n, edges, init);
            for (int i = 0; i < n; i++) {
                ans[i] |= curans[i] << bit;
            }
        }
        for (int i = 0; i < n; i++) {
            cout << ans[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
