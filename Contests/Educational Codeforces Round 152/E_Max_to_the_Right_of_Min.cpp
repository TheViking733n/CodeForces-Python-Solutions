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




struct item{
    int m;
};


struct MinSegTree{
    int size;
    vector<item> tree;

    // Utility functions   to be definitely changed as per needs
    item NEUTRAL_ELEMENT = {oo};
    item single(int a){
        return {a};
    }

    item merge(item a1, item a2){
        return {min(a1.m, a2.m)};
    }


    void init(int n){
        size = 1;
        while(size < n) size *= 2;
        tree.resize(2*size);                 //Initial value 
    }

    void build(vector<int> &a, int x, int lx, int rx){
        if(rx - lx == 1){
            if(lx < a.size()){
                tree[x] = single(a[lx]);
            }
            return;
        }
        int mid = (lx + rx) / 2;
        build(a, 2*x+1, lx, mid);
        build(a, 2*x+2, mid, rx);
        tree[x] = merge(tree[2*x+1] , tree[2*x+2]);
    }


    void build(vector<int> &a){
        build(a, 0, 0, size);
    }


    void set(int i, int v, int x, int lx, int rx){
        if(rx - lx == 1) {
            tree[x] = single(v);  
            return;
        }
        int mid = (lx + rx) >> 1;
        if(i < mid){
            set(i, v, 2*x+1, lx, mid);
        }
        else set(i, v, 2*x+2, mid, rx);
        tree[x] = merge(tree[2*x+1] , tree[2*x+2]);
    }



    void set(int i, int v){
        set(i, v, 0, 0, size);
    }



    item query(int l, int r, int x, int lx, int rx){
        if(lx >= r  ||  l >= rx) return NEUTRAL_ELEMENT;                  // Set non-interfering value for the required operation
        if(lx >= l  &&  rx <= r) return tree[x];
        int mid = (lx + rx) >> 1;
        item s1 = query(l, r, 2*x+1, lx, mid);
        item s2 = query(l, r, 2 * x + 2, mid, rx);
        return merge(s1,s2);
    }



    int query(int l, int r) {return query(l, r, 0, 0, size).m;}
};



struct MaxSegTree{
    int size;
    vector<item> tree;

    // Utility functions   to be definitely changed as per needs
    item NEUTRAL_ELEMENT = {-oo};
    item single(int a){
        return {a};
    }

    item merge(item a1, item a2){
        return {max(a1.m, a2.m)};
    }


    void init(int n){
        size = 1;
        while(size < n) size *= 2;
        tree.resize(2*size);                 //Initial value 
    }

    void build(vector<int> &a, int x, int lx, int rx){
        if(rx - lx == 1){
            if(lx < a.size()){
                tree[x] = single(a[lx]);
            }
            return;
        }
        int mid = (lx + rx) / 2;
        build(a, 2*x+1, lx, mid);
        build(a, 2*x+2, mid, rx);
        tree[x] = merge(tree[2*x+1] , tree[2*x+2]);
    }


    void build(vector<int> &a){
        build(a, 0, 0, size);
    }


    void set(int i, int v, int x, int lx, int rx){
        if(rx - lx == 1) {
            tree[x] = single(v);  
            return;
        }
        int mid = (lx + rx) >> 1;
        if(i < mid){
            set(i, v, 2*x+1, lx, mid);
        }
        else set(i, v, 2*x+2, mid, rx);
        tree[x] = merge(tree[2*x+1] , tree[2*x+2]);
    }



    void set(int i, int v){
        set(i, v, 0, 0, size);
    }



    item query(int l, int r, int x, int lx, int rx){
        if(lx >= r  ||  l >= rx) return NEUTRAL_ELEMENT;                  // Set non-interfering value for the required operation
        if(lx >= l  &&  rx <= r) return tree[x];
        int mid = (lx + rx) >> 1;
        item s1 = query(l, r, 2*x+1, lx, mid);
        item s2 = query(l, r, 2 * x + 2, mid, rx);
        return merge(s1,s2);
    }



    int query(int l, int r) {return query(l, r, 0, 0, size).m;}
};


int f(int st, int en, MinSegTree& rmn, MaxSegTree& rmx, vector<int>& arr) {
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
    MinSegTree rmn; rmn.init(n); rmn.build(a2);
    MaxSegTree rmx; rmx.init(n); rmx.build(a2);
    cout << f(0, n - 1, rmn, rmx, arr) << endl;

    return 0;
}
