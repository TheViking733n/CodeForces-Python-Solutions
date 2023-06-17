#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int &x : arr) cin >> x;
    // No effect on C++ submissions
    unordered_set<int> s;
    for (int x : arr) s.insert(x);

    cout << s.size() << endl;

    return 0;
}
