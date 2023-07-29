import sys
input = sys.stdin.readline
oo = 1 << 30
# class RangeQuery:
#     def __init__(self, data, func=min):
#         self.func = func
#         self._data = _data = [list(data)]
#         i, n = 1, len(_data[0])
#         while 2 * i <= n:
#             prev = _data[-1]
#             _data.append([func(prev[j], prev[j + i]) for j in range(n - 2 * i + 1)])
#             i <<= 1

#     def query(self, start, stop):
#         """func of data[start, stop)"""
#         depth = (stop - start).bit_length() - 1
#         return self.func(self._data[depth][start], self._data[depth][stop - (1 << depth)])

#     def __getitem__(self, idx):
#         return self._data[0][idx]

class SegmentTree:
    def __init__(self, data, default=0, func=max):
        """initialize the segment tree with data"""
        self._default = default
        self._func = func
        self._len = len(data)
        self._size = _size = 1 << (self._len - 1).bit_length()

        self.data = [default] * (2 * _size)
        self.data[_size:_size + self._len] = data
        for i in reversed(range(_size)):
            self.data[i] = func(self.data[i + i], self.data[i + i + 1])

    def __delitem__(self, idx):
        self[idx] = self._default

    def __getitem__(self, idx):
        return self.data[idx + self._size]

    def __setitem__(self, idx, value):
        idx += self._size
        self.data[idx] = value
        idx >>= 1
        while idx:
            self.data[idx] = self._func(self.data[2 * idx], self.data[2 * idx + 1])
            idx >>= 1

    def __len__(self):
        return self._len

    def query(self, start, stop):
        """func of data[start, stop)"""
        start += self._size
        stop += self._size

        res_left = res_right = self._default
        while start < stop:
            if start & 1:
                res_left = self._func(res_left, self.data[start])
                start += 1
            if stop & 1:
                stop -= 1
                res_right = self._func(self.data[stop], res_right)
            start >>= 1
            stop >>= 1

        return self._func(res_left, res_right)
    
    def max_right(self, st, func):
        """Returns r s.t. func(data[st:r]) holds, and func(data[st:r+1]) doesn't hold. O(log n)"""
        if st == self._len: return self._len
        st += self._size
        sm = self._default
        while 1:
            while st % 2 == 0: st >>= 1
            if not func(self._func(sm, self.data[st])):
                while st < self._size:
                    st = 2 * st
                    if func(self._func(sm, self.data[st])):
                        sm = self._func(sm, self.data[st])
                        st += 1
                return st - self._size
            sm = self._func(sm, self.data[st])
            st += 1
            if (st & -st) == st: break
        return self._len
    
    def min_left(self, en, func):
        """Returns l s.t. func(data[l:en]) holds, and func(data[l-1:en]) doesn't hold. O(log n)"""
        if en == 0: return 0
        en += self._size
        sm = self._default
        while 1:
            en -= 1
            while en > 1 and en % 2: en >>= 1
            if not func(self._func(self.data[en], sm)):
                while en < self._size:
                    en = 2 * en + 1
                    if func(self._func(self.data[en], sm)):
                        sm = self._func(self.data[en], sm)
                        en -= 1
                return en + 1 - self._size
            sm = self._func(self.data[en], sm)
            if (en & -en) == en: break
        return 0

    def __repr__(self):
        return "SegmentTree({0})".format(self.data)




def solveForL(st, en, L, rmn, rmx, arr, ind):
    left = L - st
    right = en - L
    ans = right
    mx = -oo

    if left < right:
        # bruteforce on left side and binary search on right side
        for i in range(L - 1, st - 1, -1):
            mx = max(mx, arr[i])
            # Find rightmost index in [L+1, en] such that max(arr[L+1..idx]) < mx
            # low = L + 1
            # high = en
            # idx = L

            # while low <= high:
            #     mid = (low + high) >> 1
            #     if rmx.query(L + 1, mid + 1) < mx:
            #         idx = mid
            #         low = mid + 1
            #     else:
            #         high = mid - 1

            idx = max(min(rmx.max_right(L + 1, lambda x: x < mx) - 1, en), L)
            # print(low, high, idx, idx2, idx - idx2)
            ans += right - idx + L
    else:
        # bruteforce on right side and binary search on left side
        for i in range(L, en + 1):
            mx = max(mx, arr[i])
            # Find leftmost index in [st, L-1] such that max(arr[idx..L-1]) < mx
            # low = st
            # high = L - 1
            # idx = L

            # while low <= high:
            #     mid = (low + high) >> 1
            #     if rmx.query(mid, L) < mx:
            #         idx = mid
            #         high = mid - 1
            #     else:
            #         low = mid + 1

            idx = min(max(rmx.min_left(L, lambda x: x < mx), st), L)

            ans += L - idx

    return ans


def solveForR(st, en, R, rmn, rmx, arr, ind):
    left = R - st
    right = en - R
    ans = left
    mn = oo

    # if left < right:
    if 0:
        # bruteforce on left side and binary search on right side
        for i in range(R - 1, st - 1, -1):
            mn = min(mn, arr[i])
            # Find rightmost index in [R+1, en] such that min(arr[R+1..idx]) > mn
            # low = R + 1
            # high = en
            # idx = R

            # while low <= high:
            #     mid = (low + high) >> 1
            #     if rmn.query(R + 1, mid + 1) > mn:
            #         idx = mid
            #         low = mid + 1
            #     else:
            #         high = mid - 1
            idx = max(min(rmn.max_right(R + 1, lambda x: x > mn) - 1, en), R)

            ans += idx - R
    else:
        # bruteforce on right side and binary search on left side
        for i in range(R + 1, en + 1):
            mn = min(mn, arr[i])
            # Find leftmost index in [st, R-1] such that min(arr[idx..R-1]) > mn
            # low = st
            # high = R - 1
            # idx = R

            # while low <= high:
            #     mid = (low + high) >> 1
            #     if rmn.query(mid, R) > mn:
            #         idx = mid
            #         high = mid - 1
            #     else:
            #         low = mid + 1
            idx = min(max(rmn.min_left(R, lambda x: x > mn), st), R)

            ans += left - R + idx

    return ans


def f(st, en, rmn, rmx, arr, ind):
    if st >= en:
        return 0

    i1 = ind[rmn.query(st, en + 1)]
    i2 = ind[rmx.query(st, en + 1)]
    ans = 0

    if i1 < i2:
        left = i1 - st + 1
        right = en - i2 + 1
        ans += left * right
        ans += solveForL(st, i2 - 1, i1, rmn, rmx, arr, ind)
        ans += solveForR(i1 + 1, en, i2, rmn, rmx, arr, ind)
    elif i1 > i2:
        i1, i2 = i2, i1
        ans += solveForR(st, i2 - 1, i1, rmn, rmx, arr, ind)
        ans += solveForL(i1 + 1, en, i2, rmn, rmx, arr, ind)

    ans += f(st, i1 - 1, rmn, rmx, arr, ind)
    ans += f(i1 + 1, i2 - 1, rmn, rmx, arr, ind)
    ans += f(i2 + 1, en, rmn, rmx, arr, ind)
    return ans


n = int(input())
arr = [int(i) - 1 for i in input().split()]
ind = [0] * n
for i in range(n): ind[arr[i]] = i

# rmn = RangeQuery(arr, min)
# rmx = RangeQuery(arr, max)
rmn = SegmentTree(arr, oo, min)
rmx = SegmentTree(arr, -oo, max)
print(f(0, n - 1, rmn, rmx, arr, ind))