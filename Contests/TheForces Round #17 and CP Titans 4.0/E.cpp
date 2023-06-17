#include <iostream>
#include <vector>
#include <unordered_map>
#include <bitset>
using namespace std;

// #define int long long int
const int MAX_N = 10001;

vector<int> spf(MAX_N + 1, 0);

void sieve() {
    spf[1] = 1;
    for (int i = 2; i <= MAX_N; i++) {
        if (spf[i] == 0) {
            spf[i] = i;
            for (int j = i * i; j <= MAX_N; j += i) {
                if (spf[j] == 0) spf[j] = i;
            }
        }
    }
}

unordered_map<int, int> factorise(int num) {
    unordered_map<int, int> ans;
    while (num > 1) {
        ans[spf[num]] += 1;
        num /= spf[num];
    }
    return ans;
}

vector<unordered_map<int, int>> facs(MAX_N + 1);

void initializeFacs() {
    for (int i = 0; i <= MAX_N; i++) {
        facs[i] = factorise(i);
    }
}

bitset<MAX_N * MAX_N> check;

int pow(int a, int b) {
    int ans = 1;
    while (b > 0) {
        if (b & 1) ans *= a;
        a *= a;
        b >>= 1;
    }
    return ans;
}

void initBitset(int k) {
    int sz = MAX_N * MAX_N;
    for (int i = 0; i <= sz; i++) {
        check[i] = false;
    }
    int i = 1, p;
    while (1) {
        p = pow(i, k);
        if (p > sz) break;
        check[p] = true;
        i++;
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    // cout.tie(NULL);
    sieve();
    initializeFacs();
    
    int TestCases = 1;

    while (TestCases--) {
        int n, k;
        cin >> n >> k;
        if (k == 1) {
            cout << ((n * (n - 1)) >> 1) << "\n";
            continue;
        }

        initBitset(k);

        vector<int> arr(n);
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        vector<int> cnt(MAX_N + 1, 0);
        for (int i : arr) {
            cnt[i]++;
        }

        int N = MAX_N;
        int ans = 0;

        for (int i = 1; i <= N; i++) {
            if (cnt[i] == 0) continue;
            for (int j = i + 1; j <= N; j++) {
                if (cnt[j] == 0) continue;
                // bool ok = true;
                // vector<int> p;
                // for (auto x : facs[i]) {
                //     p.push_back(x.first);
                // }
                // for (auto x : facs[j]) {
                //     p.push_back(x.first);
                // }
                // for (int x : p) {
                //     if ((facs[i][x] + facs[j][x]) % k) {
                //         ok = false;
                //         break;
                //     }
                // }
                // if (ok) ans += cnt[i] * cnt[j];
                int p = i * j;
                if (check[p]) ans += cnt[i] * cnt[j];
            }
        }

        for (int i = 1; i <= N; i++) {
            if (cnt[i] <= 1) continue;
            // bool ok = true;
            // for (auto x : facs[i]) {
            //     if ((2 * x.second) % k) {
            //         ok = false;
            //         break;
            //     }
            // }
            // if (ok) ans += cnt[i] * (cnt[i] - 1) >> 1;
            int p = i * i;
            if (check[p]) ans += cnt[i] * (cnt[i] - 1) >> 1;
        }

        cout << ans << "\n";
    }

    return 0;
}
