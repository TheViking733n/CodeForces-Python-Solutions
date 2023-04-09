#include <bits/stdc++.h>
using namespace std;
int main() {
    int n, queries, x, y, ans = 0; char c;
    cin >> n >> queries;
    vector<map<int, int>> jars(n+1);
    while (queries--) {
        cin >> c >> x >> y;
        if (c == '+') jars[y][x]++;
        else ans += jars[x] == jars[y];
    }
    cout << ans << endl;
    return 0;
}