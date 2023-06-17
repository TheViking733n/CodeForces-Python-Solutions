#include <iostream>
#include <vector>
using namespace std;

const int N = 1001;
vector<vector<vector<int>>> memo(N, vector<vector<int>>(N, vector<int>(2, -1)));

int f(int a, int b, int player) {
    if (memo[a][b][player] != -1) return memo[a][b][player];
    if (a == 0 && b == 0) return player ^ 1;

    for (int x = 1; x <= a; x++) {
        int p = f(a - x, b, player ^ 1);
        if (p == player) {
            memo[a][b][player] = player;
            return player;
        }
    }

    for (int x = 1; x <= b; x++) {
        int p = f(a, b - x, player ^ 1);
        if (p == player) {
            memo[a][b][player] = player;
            return player;
        }
    }

    for (int x = 1; x <= min(a, b); x++) {
        int p = f(a - x, b - x, player ^ 1);
        if (p == player) {
            memo[a][b][player] = player;
            return player;
        }
    }

    memo[a][b][player] = player ^ 1;
    return player ^ 1;
}

int main() {
    for (int p=0; p<2; p++) {
        for (int i=0; i<N; i++) {
            cout << i << "\n";
            for (int j=0; j<N; j++) {
                f(i, j, p);
            }
        }
    }
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (memo[i][j][0] == 1) {
                cout << i << " " << j << "\n";
            }
        }
    }

    return 0;
}
