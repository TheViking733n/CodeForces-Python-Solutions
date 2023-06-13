#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>
#include <algorithm>
using namespace std;

const int inf = 1 << 30;

bool isPrime(int x) {
    for (int i = 2; i < x; i++) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

int f(int x, const vector<int>& pr, const vector<int>& pi) {
    int sum = 0;
    for (int i : pr) {
        if (x % i == 0) {
            sum += pi[i];
        }
    }
    return sum;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    vector<int> primes;
    for (int i = 2; i < 59; i++) {
        if (isPrime(i)) {
            primes.push_back(i);
        }
    }

    int ln = primes.size();
    vector<int> pinverse(59, -1);
    pinverse[1] = 0;
    for (int i = 0; i < ln; i++) {
        pinverse[primes[i]] = 1 << i;
    }

    vector<int> T(61);
    for (int i = 1; i <= 59; i++) {
        T[i] = f(i, primes, pinverse);
    }

    vector<vector<int>> dp(n + 1, vector<int>(1 << ln, inf));
    fill(dp[0].begin(), dp[0].end(), 0);

    for (int j = 0; j < n; j++) {
        int v = arr[j];
        for (int c1 = 1; c1 < min(2 * v, 58); c1++) {
            int c = T[c1];
            int d = abs(v - c1);
            for (int i = 0; i < dp[0].size(); i++) {
                if (c & i) {
                    continue;
                }
                dp[j + 1][i | c] = min(dp[j + 1][i | c], (((dp[j][i] >> 6) + d) << 6) + c1);
            }
        }
    }

    int mn = *min_element(dp.back().begin(), dp.back().end());
    int i1 = find(dp.back().begin(), dp.back().end(), mn) - dp.back().begin();

    vector<int> ans;
    for (int i = n; i > 0; i--) {
        ans.push_back(dp[i][i1] & 63);
        i1 ^= T[ans.back()];
    }

    reverse(ans.begin(), ans.end());
    for (int num : ans) {
        cout << num << ' ';
    }
    cout << endl;

    return 0;
}
