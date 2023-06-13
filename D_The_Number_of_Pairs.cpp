#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <cstring>

using namespace std;
#define endl '\n'
#define int long long

const int MAX_N = 20000005;
int sp[MAX_N]; // Smallest prime of a number, for a prime p, sp[p] = p

void init_sp() {
    for (int i = 2; i < MAX_N; i += 2) {
        sp[i] = 2; // For all even numbers, its sp will be 2
    }

    for (int i = 3; i < MAX_N; i += 2) { // Now for odd numbers
        if (sp[i] == -1) {
            sp[i] = i;
            int j = i;
            while (j * i < MAX_N) {
                if (sp[j * i] == -1) {
                    sp[j * i] = i;
                }
                j += 2;
            }
        }
    }
}

int memo1[MAX_N];



int primeFactor(int n) {
    if (memo1[n] != -1) {
        return memo1[n];
    }
    int m = n;

    unordered_set<int> seen;
    while (n != 1) {
        seen.insert(sp[n]);
        n /= sp[n];
    }

    memo1[m] = seen.size();
    return seen.size();
}

void precalc() {
    // for (int i = 1; i < 10; i++) {
    //     cout << i << ":" << primeFactor(i) << " ";
    // }
    // cout << endl;
    memo1[1] = 0;
    memo1[2] = 1;
    for (int i = 3; i < MAX_N; i++) {
        int prev = i / sp[i];
        memo1[i] = memo1[prev] + (sp[i] != sp[prev]);
    }

}

void divisors(int n, vector<int>& divs) {
    for (int i = 1; i * i <= n; i++) {
        if (n % i == 0) {
            divs.push_back(i);
            if (i * i != n) {
                divs.push_back(n / i);
            }
        }
    }
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    memset(sp, -1, sizeof(sp));
    memset(memo1, -1, sizeof(memo1));
    init_sp();
    precalc();

    unordered_map<int, vector<int>> memo;

    int tt;
    cin >> tt;

    while (tt--) {
        int a, b, c;
        cin >> a >> b >> c;

        int ans = 0;
        vector<int> divs;
        if (memo.find(c) != memo.end()) {
            divs = memo[c];
        } else {
            divisors(c, divs);
            memo[c] = divs;
        }
        for (int p : divs) {
            if ((p + b) % a == 0) {
                int k = (p + b) / a;
                int pf = primeFactor(k);
                ans += 1 << pf;
            }
        }

        cout << ans << endl;
    }

    return 0;
}
