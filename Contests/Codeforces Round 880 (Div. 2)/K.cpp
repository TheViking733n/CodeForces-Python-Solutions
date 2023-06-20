#define mod 10000000;
int N = 1001;
int dp[1001][1001];

int combination(int n, int r) {
    if (dp[n][r] != -1)
        return dp[n][r];
    if (r == 0 || r == n) {
        return dp[n][r] = 1;
        return 1;
    }
    else {
        dp[n][r] = (combination(n - 1, r - 1) + combination(n - 1, r)) % mod;
        return dp[n][r];
    }
}

int paint(int input1,int input2){
    for (int i = 0; i < N; i++) {
        for (int j = 0; j <= i; j++) {
            dp[i][j] = -1;
        }
    }
    int n = input1, r = input2;
    int ans = 0;
    for (int i=1; i<=r; i++) {
        ans += combination(n, i);
        ans %= mod;
    }
    return ans;
}