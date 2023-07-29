#include <bits/stdc++.h>
#define int long long
using namespace std;
int bit_length(int x) {
    int ans = 0;
    while (x > 0) {
        x >>= 1;
        ans += 1;
    }
    return ans;
}

// int encode(int x, int y, int z) {
//     return (x << 40) | (y << 20) | z;
// }
// array<int, 3> decode(int x) {
//     return {(x >> 40), (x >> 20) & 0xfffff, x & 0xfffff};
// }

// class RangeQuery {
// public:
//     RangeQuery(const vector<int>& data, int (*func)(int, int)) : func(func) {
//         _data.push_back(data);
//         int i = 1, n = data.size();
//         while (2 * i <= n) {
//             vector<int> prev = _data.back();
//             _data.push_back(vector<int>(n - 2 * i + 1));
//             for (int j = 0; j < n - 2 * i + 1; ++j)
//                 _data.back()[j] = func(prev[j], prev[j + i]);
//             i <<= 1;
//         }
//     }

//     int query(int start, int stop) {
//         int depth = bit_length(stop - start) - 1;
//         return func(_data[depth][start], _data[depth][stop - (1 << depth)]);
//     }

//     int operator[](int idx) {
//         return _data[0][idx];
//     }

// private:
//     int (*func)(int, int);
//     vector<vector<int>> _data;
// };

const int oo = 1e9;

template<typename T> struct RangeMinQuery {
	vector<T> v;
	int n; static const int b = 30;
	vector<int> mask, t;

	int op(int x, int y) { return v[x] < v[y] ? x : y; }
	int msb(int x) { return __builtin_clz(1)-__builtin_clz(x); }
	int small(int r, int sz = b) { return r-msb(mask[r]&((1<<sz)-1)); }
	RangeMinQuery(const vector<T>& v_) : v(v_), n(v.size()), mask(n), t(n) {
		for (int i = 0, at = 0; i < n; mask[i++] = at |= 1) {
			at = (at<<1)&((1<<b)-1);
			while (at and op(i, i-msb(at&-at)) == i) at ^= at&-at;
		}
		for (int i = 0; i < n/b; i++) t[i] = small(b*i+b-1);
		for (int j = 1; (1<<j) <= n/b; j++) for (int i = 0; i+(1<<j) <= n/b; i++)
			t[n/b*j+i] = op(t[n/b*(j-1)+i], t[n/b*(j-1)+i+(1<<(j-1))]);
	}
	T query(int l, int r) {
        --r;
		if (r-l+1 <= b) return v[small(r, r-l+1)];
		int ans = op(small(l+b-1), small(r));
		int x = l/b+1, y = r/b-1;
		if (x <= y) {
			int j = msb(y-x+1);
			ans = op(ans, op(t[n/b*j+x], t[n/b*j+y-(1<<j)+1]));
		}
		return v[ans];
	}
};

template<typename T> struct RangeMaxQuery {
	vector<T> v;
	int n; static const int b = 30;
	vector<int> mask, t;

	int op(int x, int y) { return v[x] > v[y] ? x : y; }
	int msb(int x) { return __builtin_clz(1)-__builtin_clz(x); }
	int small(int r, int sz = b) { return r-msb(mask[r]&((1<<sz)-1)); }
	RangeMaxQuery(const vector<T>& v_) : v(v_), n(v.size()), mask(n), t(n) {
		for (int i = 0, at = 0; i < n; mask[i++] = at |= 1) {
			at = (at<<1)&((1<<b)-1);
			while (at and op(i, i-msb(at&-at)) == i) at ^= at&-at;
		}
		for (int i = 0; i < n/b; i++) t[i] = small(b*i+b-1);
		for (int j = 1; (1<<j) <= n/b; j++) for (int i = 0; i+(1<<j) <= n/b; i++)
			t[n/b*j+i] = op(t[n/b*(j-1)+i], t[n/b*(j-1)+i+(1<<(j-1))]);
	}
	T query(int l, int r) {
        --r;
		if (r-l+1 <= b) return v[small(r, r-l+1)];
		int ans = op(small(l+b-1), small(r));
		int x = l/b+1, y = r/b-1;
		if (x <= y) {
			int j = msb(y-x+1);
			ans = op(ans, op(t[n/b*j+x], t[n/b*j+y-(1<<j)+1]));
		}
		return v[ans];
	}
};




long long solveForL(int st, int en, int L, RangeMinQuery<int>& rmn, RangeMaxQuery<int>& rmx, vector<int>& arr, vector<int> &ind) {
    int left = L - st, right = en - L;
    long long ans = right;
    int mx = -oo;
    if (left < right) {
        // bruteforce on left side and binary search on right side
        for (int i = L-1; i >= st; i--) {
            mx = max(mx, arr[i]);
            // Find rightmost index in [L+1, en] such that max(arr[L+1..idx]) > mx
            int low = L+1, high = en, idx = L;
            while (low <= high) {
                int mid = low + high + 1 >> 1;
                if (rmx.query(L+1, mid+1) > mx) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            ans += idx - L;
        }
    } else {
        // bruteforce on right side and binary search on left side
        for (int i = L+1; i <= en; i++) {
            mx = max(mx, arr[i]);
            // Find leftmost index in [st, L-1] such that max(arr[idx..L-1]) < mx
            int low = st, high = L-1, idx = L;
            while (low <= high) {
                int mid = low + high >> 1;
                if (rmn.query(mid, L) < mx) {
                    idx = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            ans += L - idx;
        }
    }
    return ans;
}

long long solveForR(int st, int en, int R, RangeMinQuery<int>& rmn, RangeMaxQuery<int>& rmx, vector<int>& arr, vector<int> &ind) {
    int left = R - st, right = en - R;
    long long ans = left;
    int mn = oo;
    if (left < right) {
        // bruteforce on left side and binary search on right side
        for (int i = R-1; i >= st; i--) {
            mn = min(mn, arr[i]);
            // Find rightmost index in [R+1, en] such that min(arr[R+1..idx]) > mn
            int low = R+1, high = en, idx = R;
            while (low <= high) {
                int mid = low + high + 1 >> 1;
                if (rmn.query(R+1, mid+1) > mn) {
                    idx = mid;
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
            ans += idx - R;
        }
    } else {
        // bruteforce on right side and binary search on left side
        for (int i = R+1; i <= en; i++) {
            mn = min(mn, arr[i]);
            // Find leftmost index in [st, R-1] such that min(arr[idx..R-1]) < mn
            int low = st, high = R-1, idx = R;
            while (low <= high) {
                int mid = low + high >> 1;
                if (rmx.query(mid, R) < mn) {
                    idx = mid;
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            }
            ans += R - idx;
        }
    }
    return ans;

}

long long f(int st, int en, RangeMinQuery<int>& rmn, RangeMaxQuery<int>& rmx, vector<int>& arr, vector<int> &ind) {
    if (st >= en)
        return 0;

    int i1 = ind[rmn.query(st, en + 1)];
    int i2 = ind[rmx.query(st, en + 1)];
    // int i1 = rmn.query(st, en + 1) & 0xfffff;
    // int i2 = rmx.query(st, en + 1) & 0xfffff;
    long long ans = 0;

    if (i1 < i2) {
        int left = i1 - st + 1;
        int right = en - i2 + 1;
        ans += (long long)left * right;
        // cout << st << " " << en << " " << i1 << " " << i2 << endl;

        ans += solveForL(st, i2-1, i1, rmn, rmx, arr, ind);
        ans += solveForR(i1+1, en, i2, rmn, rmx, arr, ind);

        // if (st == i1) {
        //     ans += i2 - i1 - 1;
        // } else {
        //     int mx = -oo;
        //     for (int i = i1 + 1; i < i2; ++i) {
        //         mx = max(mx, arr[i]);
        //         // Find leftmost index in [st, i1] such that max(arr[idx..i1]) < mx
        //         int low = st, high = i1, idx = i1;
        //         while (low <= high) {
        //             int mid = (low + high) >> 1;
        //             if ((rmx.query(mid, i1 + 1)) < mx) {
        //                 high = mid - 1;
        //                 idx = mid;
        //             } else {
        //                 low = mid + 1;
        //             }
        //         }
        //         ans += i1 - idx + 1;
        //     }
        // }


        // if (i2 == en) {
        //     ans += i2 - i1 - 1;

        // } else {
        //     int mn = oo;
        //     for (int i = i2 - 1; i > i1; --i) {
        //         mn = min(mn, arr[i]);
        //         // Find rightmost index in [i2, en] such that min(arr[i2..idx]) > mn
        //         int low = i2, high = en, idx = i2;
        //         while (low <= high) {
        //             int mid = (low + high) >> 1;
        //             if ((rmn.query(i2, mid + 1)) > mn) {
        //                 low = mid + 1;
        //                 idx = mid;
        //             } else {
        //                 high = mid - 1;
        //             }
        //         }
        //         ans += idx - i2 + 1;
        //     }
        // }

    } else if (i1 > i2) {
        swap(i1, i2);

        ans += solveForR(st, i2-1, i1, rmn, rmx, arr, ind);
        ans += solveForL(i1+1, en, i2, rmn, rmx, arr, ind);

        // int mn = oo, mx = -oo;
        // for (int i = i1 - 1; i >= st; --i) {
        //     mn = min(mn, arr[i]);
        //     // Find rightmost index in [i1, i2-1] such that min(arr[i1..idx]) > mn
        //     int low = i1, high = i2 - 1, idx = i1;
        //     while (low <= high) {
        //         int mid = (low + high) >> 1;
        //         if ((rmn.query(i1, mid + 1)) > mn) {
        //             low = mid + 1;
        //             idx = mid;
        //         } else {
        //             high = mid - 1;
        //         }
        //     }
        //     ans += idx - i1 + 1;
        // }

        // for (int i = i2 + 1; i <= en; ++i) {
        //     mx = max(mx, arr[i]);
        //     // Find leftmost index in [i1+1, i2] such that max(arr[idx..i2]) < mx
        //     int low = i1 + 1, high = i2, idx = i2;
        //     while (low <= high) {
        //         int mid = (low + high) >> 1;
        //         if ((rmx.query(mid, i2 + 1)) < mx) {
        //             high = mid - 1;
        //             idx = mid;
        //         } else {
        //             low = mid + 1;
        //         }
        //     }
        //     ans += i2 - idx + 1;
        // }
    }

    ans += f(st, i1 - 1, rmn, rmx, arr, ind);
    ans += f(i1 + 1, i2 - 1, rmn, rmx, arr, ind);
    ans += f(i2 + 1, en, rmn, rmx, arr, ind);
    return ans;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n);
    vector<int> ind(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        --arr[i];
        // arr[i] = i;
        ind[arr[i]] = i;
    }

    // vector<int> a2(n);
    // for (int i = 0; i < n; ++i)
    //     // a2[i] = (arr[i] << 20) | i;
    //     a2[i] = encode(arr[i], arr[i], i);
    
    // auto Min = [](int x, int y) -> int { return x < y ? x : y; };
    // auto Max = [](int x, int y) -> int { return x > y ? x : y; };

    RangeMinQuery<int> rmn(arr);
    RangeMaxQuery<int> rmx(arr);

    // RangeQuery rmn(a2, Min);
    // RangeQuery rmx(a2, Max);

    cout << f(0, n - 1, rmn, rmx, arr, ind) << endl;

    return 0;
}
