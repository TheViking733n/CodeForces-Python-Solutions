#include <bits/stdc++.h>

using namespace std;

// using cd = complex<double>;
// const double PI = acos(-1);

// void fft(vector<cd> & a, bool invert) {
//     int n = a.size();

//     for (int i = 1, j = 0; i < n; i++) {
//         int bit = n >> 1;
//         for (; j & bit; bit >>= 1)
//             j ^= bit;
//         j ^= bit;

//         if (i < j)
//             swap(a[i], a[j]);
//     }

//     for (int len = 2; len <= n; len <<= 1) {
//         double ang = 2 * PI / len * (invert ? -1 : 1);
//         cd wlen(cos(ang), sin(ang));
//         for (int i = 0; i < n; i += len) {
//             cd w(1);
//             for (int j = 0; j < len / 2; j++) {
//                 cd u = a[i+j], v = a[i+j+len/2] * w;
//                 a[i+j] = u + v;
//                 a[i+j+len/2] = u - v;
//                 w *= wlen;
//             }
//         }
//     }

//     if (invert) {
//         for (cd & x : a)
//             x /= n;
//     }
// }

// vector<double> conv(vector<int> &a, vector<int> &b, int mod) {
//     int s = a.size() + b.size() - 1;
//     int n = 1;
//     while (n < s) n <<= 1;
//     cout << n << endl;
//     // while (a.size() < n) a.push_back(0);
//     // while (b.size() < n) b.push_back(0);
//     cd zero(0.0, 0.0);
//     vector<cd> A(n, zero), B(n, zero);
//     for (int i = 0; i < a.size(); i++) {
//         cd temp(a[i], 0.0);
//         A[i] = temp;
//     }
//     for (int i = 0; i < b.size(); i++) {
//         cd temp(b[i], 0.0);
//         B[i] = temp;
//     }
//     fft(A, 0);
//     fft(B, 0);
//     for (int i = 0; i < n; i++) A[i] *= B[i];
//     fft(A, 1);
//     vector<double> ans;
//     for (int i = 0; i < s; i++) ans.push_back(real(A[i]));
//     return ans;
// }

#define int long long
const double PI = acos(-1.0);

struct Complex {
    double real, imag;
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}
    Complex operator +(const Complex &o) const {
        return Complex(real + o.real, imag + o.imag);
    }
    Complex operator -(const Complex &o) const {
        return Complex(real - o.real, imag - o.imag);
    }
    Complex operator *(const Complex &o) const {
        return Complex(real * o.real - imag * o.imag, real * o.imag + imag * o.real);
    }
};

vector<Complex> FFT(vector<Complex> a, bool invert) {
    int n = a.size();
    if (n == 1) return a;

    vector<Complex> even(n / 2), odd(n / 2);
    for (int i = 0, j = 0; i < n; i += 2, ++j) {
        even[j] = a[i];
        odd[j] = a[i + 1];
    }

    vector<Complex> y0 = FFT(even, invert), y1 = FFT(odd, invert);
    double ang = 2 * PI / n * (invert ? -1 : 1);
    Complex w(1), wn(cos(ang), sin(ang));
    vector<Complex> y(n);
    for (int i = 0; i < n / 2; ++i) {
        y[i] = y0[i] + w * y1[i];
        y[i + n / 2] = y0[i] - w * y1[i];
        if (invert) {
            y[i] = Complex(y[i].real / 2, y[i].imag / 2);
            y[i + n / 2] = Complex(y[i + n / 2].real / 2, y[i + n / 2].imag / 2);
        }
        w = w * wn;
    }
    return y;
}

vector<int> conv(vector<int> a, vector<int> b, int mod) {
    int s = a.size() + b.size() - 1;
    int n = 1, m = max(a.size(), b.size());
    while (n < m) n <<= 1;
    n <<= 1;

    vector<Complex> fa(a.begin(), a.end()), fb(b.begin(), b.end());
    fa.resize(n), fb.resize(n);

    fa = FFT(fa, false), fb = FFT(fb, false);
    for (int i = 0; i < n; ++i) fa[i] = fa[i] * fb[i];
    fa = FFT(fa, true);

    vector<int> result(s);
    for (int i = 0; i < s; ++i) result[i] = ((int)(fa[i].real + 0.5) + 3 * mod) % mod;
    return result;
}

vector<int> bin_exp_fft_conv(vector<int> pol, int exp, int mod) {
    vector<int> ans{1};
    while (exp > 0) {
        if (exp & 1) ans = conv(ans, pol, mod);
        exp >>= 1;
        pol = conv(pol, pol, mod);
    }
    return ans;
}

signed main() {
    int n, mod;
    cin >> n >> mod;
    vector<int> pol{1, 1};
    vector<int> ans = bin_exp_fft_conv(pol, n, mod);
    for (int i = 0; i < ans.size(); ++i) cout << ans[i] << ' ';
    cout << endl;
    return 0;
}
