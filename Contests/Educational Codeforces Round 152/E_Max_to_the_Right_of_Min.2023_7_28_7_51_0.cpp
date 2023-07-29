#include <bits/stdc++.h>
using namespace std;
#define int long long
int oo = 1e18;

int bit_length(int x) {
    int ans = 0;
    while (x > 0) {
        x >>= 1;
        ans += 1;
    }
    return ans;
}

class RangeQuery {
public:
    RangeQuery(const vector<int>& data, int (*func)(int, int)) : func(func) {
        _data.push_back(data);
        int i = 1, n = data.size();
        while (2 * i <= n) {
            vector<int> prev = _data.back();
            _data.push_back(vector<int>(n - 2 * i + 1));
            for (int j = 0; j < n - 2 * i + 1; ++j)
                _data.back()[j] = func(prev[j], prev[j + i]);
            i <<= 1;
        }
    }

    int query(int start, int stop) {
        int depth = bit_length(stop - start) - 1;
        return func(_data[depth][start], _data[depth][stop - (1 << depth)]);
    }

    int operator[](int idx) {
        return _data[0][idx];
    }

private:
    int (*func)(int, int);
    vector<vector<int>> _data;
};



class SegmentTree {
public:
    SegmentTree(const vector<int>& data, int (*func)(int, int)) : func(func) {
        int n = data.size();
        tree.resize(4 * n);
        build(data, 0, 0, n - 1);
    }

    int query(int start, int stop) {
        return queryHelper(0, 0, data.size() - 1, start, stop);
    }

    int operator[](int idx) {
        return data[idx];
    }

private:
    int (*func)(int, int);
    vector<int> tree;
    vector<int> data;

    int leftChild(int i) { return 2 * i + 1; }
    int rightChild(int i) { return 2 * i + 2; }

    int build(const vector<int>& arr, int node, int start, int end) {
        if (start == end) {
            tree[node] = arr[start];
            return tree[node];
        }

        int mid = start + (end - start) / 2;
        int leftVal = build(arr, leftChild(node), start, mid);
        int rightVal = build(arr, rightChild(node), mid + 1, end);
        tree[node] = func(leftVal, rightVal);
        return tree[node];
    }

    int queryHelper(int node, int start, int end, int queryStart, int queryEnd) {
        if (queryStart <= start && end <= queryEnd) {
            return tree[node];
        }

        if (queryEnd <= start || end <= queryStart) {
            return func(0, 0); // Modify this line based on the neutral value of the function
        }

        int mid = start + (end - start) / 2;
        int leftVal = queryHelper(leftChild(node), start, mid, queryStart, queryEnd);
        int rightVal = queryHelper(rightChild(node), mid + 1, end, queryStart, queryEnd);
        return func(leftVal, rightVal);
    }
};


int f(int st, int en, SegmentTree& rmn, SegmentTree& rmx, vector<int>& arr) {
    if (st >= en)
        return 0;

    int i1 = rmn.query(st, en + 1) & 0xfffff;
    int i2 = rmx.query(st, en + 1) & 0xfffff;
    int ans = 0;

    if (i1 < i2) {
        int left = i1 - st + 1;
        int mid = i2 - i1 - 1;
        int right = en - i2 + 1;
        ans += left * right;

        int mx = -oo;
        for (int i = i1 + 1; i < i2; ++i) {
            mx = max(mx, arr[i]);
            // Find leftmost index in [st, i1] such that max(arr[idx..i1]) < mx
            int low = st, high = i1, idx = i1;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if ((rmx.query(mid, i1 + 1) >> 20) < mx) {
                    high = mid - 1;
                    idx = mid;
                } else {
                    low = mid + 1;
                }
            }
            ans += i1 - idx + 1;
        }

        int mn = oo;
        for (int i = i2 - 1; i > i1; --i) {
            mn = min(mn, arr[i]);
            // Find rightmost index in [i2, en] such that min(arr[i2..idx]) > mn
            int low = i2, high = en, idx = i2;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if ((rmn.query(i2, mid + 1) >> 20) > mn) {
                    low = mid + 1;
                    idx = mid;
                } else {
                    high = mid - 1;
                }
            }
            ans += idx - i2 + 1;
        }
    } else if (i1 > i2) {
        swap(i1, i2);
        int mn = oo, mx = -oo;
        for (int i = i1 - 1; i >= st; --i) {
            mn = min(mn, arr[i]);
            // Find rightmost index in [i1, i2-1] such that min(arr[i1..idx]) > mn
            int low = i1, high = i2 - 1, idx = i1;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if ((rmn.query(i1, mid + 1) >> 20) > mn) {
                    low = mid + 1;
                    idx = mid;
                } else {
                    high = mid - 1;
                }
            }
            ans += idx - i1 + 1;
        }

        for (int i = i2 + 1; i <= en; ++i) {
            mx = max(mx, arr[i]);
            // Find leftmost index in [i1+1, i2] such that max(arr[idx..i2]) < mx
            int low = i1 + 1, high = i2, idx = i2;
            while (low <= high) {
                int mid = (low + high) >> 1;
                if ((rmx.query(mid, i2 + 1) >> 20) < mx) {
                    high = mid - 1;
                    idx = mid;
                } else {
                    low = mid + 1;
                }
            }
            ans += i2 - idx + 1;
        }
    }

    ans += f(st, i1 - 1, rmn, rmx, arr);
    ans += f(i1 + 1, i2 - 1, rmn, rmx, arr);
    ans += f(i2 + 1, en, rmn, rmx, arr);
    return ans;
}

signed main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n; ++i) {
        cin >> arr[i];
        arr[i] -= 1;
    }

    vector<int> a2(n);
    for (int i = 0; i < n; ++i)
        a2[i] = (arr[i] << 20) | i;
    
    auto Min = [](int x, int y) -> int { return x < y ? x : y; };
    auto Max = [](int x, int y) -> int { return x > y ? x : y; };

    // RangeQuery rmn(a2, Min);
    // RangeQuery rmx(a2, Max);
    SegmentTree rmn(a2, Min);
    SegmentTree rmx(a2, Max);
    cout << 1 << endl;
    cout << f(0, n - 1, rmn, rmx, arr) << endl;
    cout << 1 << endl;

    return 0;
}
