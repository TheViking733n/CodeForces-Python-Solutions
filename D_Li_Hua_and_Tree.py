from __future__ import division, print_function
import os,sys
from io import BytesIO, IOBase
from random import randint, randrange
if sys.version_info[0] < 3:
    from __builtin__ import xrange as range
    from future_builtins import ascii, filter, hex, map, oct, zip


from math import ceil, floor, factorial, log10
# from math import log,sqrt,cos,tan,sin,radians
from bisect import bisect_left, bisect_right
from collections import deque, Counter, defaultdict
# from bisect import bisect,bisect_left,bisect_right,insort,insort_left,insort_right
# from decimal import *
# from heapq import nsmallest, nlargest, heapify, heappop, heappush, heapreplace
# from collections import OrderedDict
# from itertools import permutations

M = 123







# class TreeNode:
#     def __init__(self, k, v):
#         self.key = k
#         self.value = v
#         self.left = None
#         self.right = None
#         self.parent = None
#         self.height = 1
#         self.num_left = 1
#         self.num_total = 1
 
 
# class AvlTree:
 
#     def __init__(self):
#         self._tree = None
 
#     def add(self, k, v):
#         if not self._tree:
#             self._tree = TreeNode(k, v)
#             return
#         node = self._add(k, v)
#         if node:
#             self._rebalance(node)
 
#     def _add(self, k, v):
#         node = self._tree
#         while node:
#             if k < node.key:
#                 if node.left:
#                     node = node.left
#                 else:
#                     node.left = TreeNode(k, v)
#                     node.left.parent = node
#                     return node.left
#             elif node.key < k:
#                 if node.right:
#                     node = node.right
#                 else:
#                     node.right = TreeNode(k, v)
#                     node.right.parent = node
#                     return node.right
#             else:
#                 node.value = v
#                 return
 
#     @staticmethod
#     def get_height(x):
#         return x.height if x else 0
 
#     @staticmethod
#     def get_num_total(x):
#         return x.num_total if x else 0
 
#     def _rebalance(self, node):
 
#         n = node
#         while n:
#             lh = self.get_height(n.left)
#             rh = self.get_height(n.right)
#             n.height = max(lh, rh) + 1
#             balance_factor = lh - rh
#             n.num_total = 1 + self.get_num_total(n.left) + self.get_num_total(n.right)
#             n.num_left = 1 + self.get_num_total(n.left)
 
#             if balance_factor > 1:
#                 if self.get_height(n.left.left) < self.get_height(n.left.right):
#                     self._rotate_left(n.left)
#                 self._rotate_right(n)
#             elif balance_factor < -1:
#                 if self.get_height(n.right.right) < self.get_height(n.right.left):
#                     self._rotate_right(n.right)
#                 self._rotate_left(n)
#             else:
#                 n = n.parent
 
#     def _remove_one(self, node):
#         """
#         Side effect!!! Changes node. Node should have exactly one child
#         """
#         replacement = node.left or node.right
#         if node.parent:
#             if AvlTree._is_left(node):
#                 node.parent.left = replacement
#             else:
#                 node.parent.right = replacement
#             replacement.parent = node.parent
#             node.parent = None
#         else:
#             self._tree = replacement
#             replacement.parent = None
#         node.left = None
#         node.right = None
#         node.parent = None
#         self._rebalance(replacement)
 
#     def _remove_leaf(self, node):
#         if node.parent:
#             if AvlTree._is_left(node):
#                 node.parent.left = None
#             else:
#                 node.parent.right = None
#             self._rebalance(node.parent)
#         else:
#             self._tree = None
#         node.parent = None
#         node.left = None
#         node.right = None
 
#     def remove(self, k):
#         node = self._get_node(k)
#         if not node:
#             return
#         if AvlTree._is_leaf(node):
#             self._remove_leaf(node)
#             return
#         if node.left and node.right:
#             nxt = AvlTree._get_next(node)
#             node.key = nxt.key
#             node.value = nxt.value
#             if self._is_leaf(nxt):
#                 self._remove_leaf(nxt)
#             else:
#                 self._remove_one(nxt)
#             self._rebalance(node)
#         else:
#             self._remove_one(node)
 
#     def get(self, k):
#         node = self._get_node(k)
#         return node.value if node else -1
 
#     def _get_node(self, k):
#         if not self._tree:
#             return None
#         node = self._tree
#         while node:
#             if k < node.key:
#                 node = node.left
#             elif node.key < k:
#                 node = node.right
#             else:
#                 return node
#         return None
 
#     def get_at(self, pos):
#         x = pos + 1
#         node = self._tree
#         while node:
#             if x < node.num_left:
#                 node = node.left
#             elif node.num_left < x:
#                 x -= node.num_left
#                 node = node.right
#             else:
#                 return (node.key, node.value)
#         raise IndexError("Out of ranges")
 
#     @staticmethod
#     def _is_left(node):
#         return node.parent.left and node.parent.left == node
 
#     @staticmethod
#     def _is_leaf(node):
#         return node.left is None and node.right is None
 
#     def _rotate_right(self, node):
#         if not node.parent:
#             self._tree = node.left
#             node.left.parent = None
#         elif AvlTree._is_left(node):
#             node.parent.left = node.left
#             node.left.parent = node.parent
#         else:
#             node.parent.right = node.left
#             node.left.parent = node.parent
#         bk = node.left.right
#         node.left.right = node
#         node.parent = node.left
#         node.left = bk
#         if bk:
#             bk.parent = node
#         node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
#         node.num_total = 1 + self.get_num_total(node.left) + self.get_num_total(node.right)
#         node.num_left = 1 + self.get_num_total(node.left)
 
#     def _rotate_left(self, node):
#         if not node.parent:
#             self._tree = node.right
#             node.right.parent = None
#         elif AvlTree._is_left(node):
#             node.parent.left = node.right
#             node.right.parent = node.parent
#         else:
#             node.parent.right = node.right
#             node.right.parent = node.parent
#         bk = node.right.left
#         node.right.left = node
#         node.parent = node.right
#         node.right = bk
#         if bk:
#             bk.parent = node
#         node.height = max(self.get_height(node.left), self.get_height(node.right)) + 1
#         node.num_total = 1 + self.get_num_total(node.left) + self.get_num_total(node.right)
#         node.num_left = 1 + self.get_num_total(node.left)
 
#     @staticmethod
#     def _get_next(node):
#         if not node.right:
#             return node.parent
#         n = node.right
#         while n.left:
#             n = n.left
#         return n
 

#     def isEmpty(self):
#         return self._tree is None




import random


class TreapMultiSet(object):
    root = 0
    size = 0

    def __init__(self, data=None):
        if data:
            data = sorted(data)
            self.root = treap_builder(data)
            self.size = len(data)

    def add(self, key):
        self.root = treap_insert(self.root, key)
        self.size += 1

    def remove(self, key):
        self.root = treap_erase(self.root, key)
        self.size -= 1

    def discard(self, key):
        try:
            self.remove(key)
        except KeyError:
            pass

    def ceiling(self, key):
        x = treap_ceiling(self.root, key)
        return treap_keys[x] if x else None

    def higher(self, key):
        x = treap_higher(self.root, key)
        return treap_keys[x] if x else None

    def floor(self, key):
        x = treap_floor(self.root, key)
        return treap_keys[x] if x else None

    def lower(self, key):
        x = treap_lower(self.root, key)
        return treap_keys[x] if x else None

    def max(self):
        return treap_keys[treap_max(self.root)]

    def min(self):
        return treap_keys[treap_min(self.root)]

    def __len__(self):
        return self.size

    def __nonzero__(self):
        return bool(self.root)

    __bool__ = __nonzero__

    def __contains__(self, key):
        return self.floor(key) == key

    def __repr__(self):
        return "TreapMultiSet({})".format(list(self))

    def __iter__(self):
        if not self.root:
            return iter([])
        out = []
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node > 0:
                if right_child[node]:
                    stack.append(right_child[node])
                stack.append(~node)
                if left_child[node]:
                    stack.append(left_child[node])
            else:
                out.append(treap_keys[~node])
        return iter(out)


# class TreapSet(TreapMultiSet):
#     def add(self, key):
#         self.root, duplicate = treap_insert_unique(self.root, key)
#         if not duplicate:
#             self.size += 1

#     def __repr__(self):
#         return "TreapSet({})".format(list(self))


# class TreapHashSet(TreapMultiSet):
#     def __init__(self, data=None):
#         if data:
#             self.keys = set(data)
#             super(TreapHashSet, self).__init__(self.keys)
#         else:
#             self.keys = set()

#     def add(self, key):
#         if key not in self.keys:
#             self.keys.add(key)
#             super(TreapHashSet, self).add(key)

#     def remove(self, key):
#         self.keys.remove(key)
#         super(TreapHashSet, self).remove(key)

#     def discard(self, key):
#         if key in self.keys:
#             self.remove(key)

#     def __contains__(self, key):
#         return key in self.keys

#     def __repr__(self):
#         return "TreapHashSet({})".format(list(self))


# class TreapHashMap(TreapMultiSet):
#     def __init__(self, data=None):
#         if data:
#             self.map = dict(data)
#             super(TreapHashMap, self).__init__(self.map.keys())
#         else:
#             self.map = {}

#     def __setitem__(self, key, value):
#         if key not in self.map:
#             super(TreapHashMap, self).add(key)
#         self.map[key] = value

#     def __getitem__(self, key):
#         return self.map[key]

#     def add(self, key):
#         raise TypeError("add on TreapHashMap")

#     def get(self, key, default=None):
#         return self.map.get(key, default=default)

#     def remove(self, key):
#         self.map.pop(key)
#         super(TreapHashMap, self).remove(key)

#     def discard(self, key):
#         if key in self.map:
#             self.remove(key)

#     def __contains__(self, key):
#         return key in self.map

#     def __repr__(self):
#         return "TreapHashMap({})".format(list(self))


left_child = [0]
right_child = [0]
treap_keys = [0]
treap_prior = [0.0]


def treap_builder(sorted_data):
    """Build a treap in O(n) time using sorted data"""
    def build(begin, end):
        if begin == end:
            return 0
        mid = (begin + end) // 2
        root = treap_create_node(sorted_data[mid])
        left_child[root] = build(begin, mid)
        right_child[root] = build(mid + 1, end)

        # sift down the priorities
        ind = root
        while True:
            lc = left_child[ind]
            rc = right_child[ind]

            if lc and treap_prior[lc] > treap_prior[ind]:
                if rc and treap_prior[rc] > treap_prior[lc]:
                    treap_prior[ind], treap_prior[rc] = treap_prior[rc], treap_prior[ind]
                    ind = rc
                else:
                    treap_prior[ind], treap_prior[lc] = treap_prior[lc], treap_prior[ind]
                    ind = lc
            elif rc and treap_prior[rc] > treap_prior[ind]:
                treap_prior[ind], treap_prior[rc] = treap_prior[rc], treap_prior[ind]
                ind = rc
            else:
                break
        return root

    return build(0, len(sorted_data))


def treap_create_node(key):
    treap_keys.append(key)
    treap_prior.append(random.random())
    left_child.append(0)
    right_child.append(0)
    return len(treap_keys) - 1


def treap_split(root, key):
    left_pos = right_pos = 0
    while root:
        if key < treap_keys[root]:
            left_child[right_pos] = right_pos = root
            root = left_child[root]
        else:
            right_child[left_pos] = left_pos = root
            root = right_child[root]
    left, right = right_child[0], left_child[0]
    right_child[left_pos] = left_child[right_pos] = right_child[0] = left_child[0] = 0
    return left, right


def treap_merge(left, right):
    where, pos = left_child, 0
    while left and right:
        if treap_prior[left] > treap_prior[right]:
            where[pos] = pos = left
            where = right_child
            left = right_child[left]
        else:
            where[pos] = pos = right
            where = left_child
            right = left_child[right]
    where[pos] = left or right
    node = left_child[0]
    left_child[0] = 0
    return node


def treap_insert(root, key):
    if not root:
        return treap_create_node(key)
    left, right = treap_split(root, key)
    return treap_merge(treap_merge(left, treap_create_node(key)), right)


def treap_insert_unique(root, key):
    if not root:
        return treap_create_node(key), False
    left, right = treap_split(root, key)
    if left and treap_keys[left] == key:
        return treap_merge(left, right), True
    return treap_merge(treap_merge(left, treap_create_node(key)), right), False


def treap_erase(root, key):
    if not root:
        raise KeyError(key)
    if treap_keys[root] == key:
        return treap_merge(left_child[root], right_child[root])
    node = root
    while root and treap_keys[root] != key:
        parent = root
        root = left_child[root] if key < treap_keys[root] else right_child[root]
    if not root:
        raise KeyError(key)
    if root == left_child[parent]:
        left_child[parent] = treap_merge(left_child[root], right_child[root])
    else:
        right_child[parent] = treap_merge(left_child[root], right_child[root])

    return node


def treap_ceiling(root, key):
    while root and treap_keys[root] < key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = treap_keys[root]
    while root:
        if treap_keys[root] < key:
            root = right_child[root]
        else:
            if treap_keys[root] < min_key:
                min_key = treap_keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def treap_higher(root, key):
    while root and treap_keys[root] <= key:
        root = right_child[root]
    if not root:
        return 0
    min_node = root
    min_key = treap_keys[root]
    while root:
        if treap_keys[root] <= key:
            root = right_child[root]
        else:
            if treap_keys[root] < min_key:
                min_key = treap_keys[root]
                min_node = root
            root = left_child[root]
    return min_node


def treap_floor(root, key):
    while root and treap_keys[root] > key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = treap_keys[root]
    while root:
        if treap_keys[root] > key:
            root = left_child[root]
        else:
            if treap_keys[root] > max_key:
                max_key = treap_keys[root]
                max_node = root
            root = right_child[root]
    return max_node


def treap_lower(root, key):
    while root and treap_keys[root] >= key:
        root = left_child[root]
    if not root:
        return 0
    max_node = root
    max_key = treap_keys[root]
    while root:
        if treap_keys[root] >= key:
            root = left_child[root]
        else:
            if treap_keys[root] > max_key:
                max_key = treap_keys[root]
                max_node = root
            root = right_child[root]
    return max_node


def treap_min(root):
    if not root:
        raise ValueError("min on empty treap")
    while left_child[root]:
        root = left_child[root]
    return root


def treap_max(root):
    if not root:
        raise ValueError("max on empty treap")
    while right_child[root]:
        root = right_child[root]
    return root


















def encode(sz, idx):
    return -((sz << 20) | (idx ^ 0xfffff))
    # return (-sz, idx)

def decode(x):
    x = -x
    return (x >> 20, (x & 0xfffff) ^ 0xfffff)
    # return -x[0], x[1]

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def dfs(u, p, g, importance, size, tree, parent, arr):
    parent[u] = p
    sz = imp = 0
    for v in g[u]:
        if v != p:
            yield dfs(v, u, g, importance, size, tree, parent, arr)
            sz += size[v]
            imp += importance[v]
            tree[u].add(encode(size[v], v))
            # tree[u][encode(size[v], v)] = encode(size[v], v)
    size[u] = sz + 1
    importance[u] = imp + arr[u]
    yield
    
 
 
def main():
    TestCases = 1
    
    for _ in range(TestCases):
        n, qq = [int(i) for i in input().split()]
        arr = [int(i) for i in input().split()]
        g = [[] for i in range(n)]
        for _ in range(n - 1):
            u, v = [int(i) - 1 for i in input().split()]
            g[u].append(v)
            g[v].append(u)
        
        imp = [0] * n
        size = [0] * n
        parent = [-1] * n
        tree = [TreapMultiSet() for i in range(n)]
        dfs(0, -1, g, imp, size, tree, parent, arr)
 
        for _ in range(qq):
            q, x = [int(i) - 1 for i in input().split()]
 
            if q == 0:
                print(imp[x])
                continue
 
            if not tree[x]:
                continue
 
            par, node = parent[x], x

            # mn = tree[node].extractMin()
            mn = tree[node].min()
            tree[node].remove(mn)

            # del tree[node][mn]
            # tree[node].remove(mn)
            sz, ch = decode(mn)
            tree[par].remove(encode(size[node], node))
            # del tree[par][encode(size[node], node)]
 
            imp[node], imp[ch] = imp[node] - imp[ch], imp[node]
            size[node], size[ch] = size[node] - size[ch], size[node]
 
            tree[par].add(encode(size[ch], ch))
            tree[ch].add(encode(size[node], node))
            # tree[par][encode(size[ch], ch)] = encode(size[ch], ch)
            # tree[ch][encode(size[node], node)] = encode(size[node], node)
 
            parent[node], parent[ch] = ch, par
        
        
        
        
        



# def dfs(u, p, g, importance, size, tree, parent, arr):
#     parent[u] = p
#     sz = imp = 0
#     for v in g[u]:
#         if v != p:
#             yield dfs(v, u, g, importance, size, tree, parent, arr)
#             sz += size[v]
#             imp += importance[v]
#             # tree[u].insert(encode(size[v], v))
#             heappush(tree[u], encode(size[v], v))
#     size[u] = sz + 1
#     importance[u] = imp + arr[u]
#     yield
    


# def main():
#     TestCases = 1
    
#     for _ in range(TestCases):
#         n, qq = [int(i) for i in input().split()]
#         arr = [int(i) for i in input().split()]
#         g = [[] for i in range(n)]
#         for _ in range(n - 1):
#             u, v = [int(i) - 1 for i in input().split()]
#             g[u].append(v)
#             g[v].append(u)
        
#         imp = [0] * n
#         size = [0] * n
#         parent = [-1] * n
#         tree = [[] for i in range(n)]
#         dfs(0, -1, g, imp, size, tree, parent, arr)

#         deleted = [set() for i in range(n)]

#         for _ in range(qq):
#             q, x = [int(i) - 1 for i in input().split()]

#             if q == 0:
#                 print(imp[x])
#                 continue
            
#             while tree[x] and tree[x][0] in deleted[x]:
#                 heappop(tree[x])

#             if not tree[x]:
#                 continue

#             par, node = parent[x], x

#             # sz, ch = decode(tree[node].pop())
#             sz, ch = decode(heappop(tree[node]))
#             # val = tree[node].get_max()
#             # sz, ch = decode(val)
#             # tree[node].remove(val)
#             # tree[par].remove(encode(size[node], node))
#             deleted[par].add(encode(size[node], node))

#             imp[node], imp[ch] = imp[node] - imp[ch], imp[node]
#             size[node], size[ch] = size[node] - size[ch], size[node]

#             # tree[par].insert(encode(size[ch], ch))
#             # tree[ch].insert(encode(size[node], node))
#             heappush(tree[par], encode(size[ch], ch))
#             heappush(tree[ch], encode(size[node], node))
#             try: deleted[par].remove(encode(size[ch], ch))
#             except: pass
#             try: deleted[ch].remove(encode(size[node], node))
#             except: pass

#             parent[node], parent[ch] = ch, par
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# ======================== Functions declaration Starts ========================
abc='abcdefghijklmnopqrstuvwxyz'
abd={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11,'m':12,'n':13,'o':14,'p':15,'q':16,'r':17,'s':18,'t':19,'u':20,'v':21,'w':22,'x':23,'y':24,'z':25}

def copy2d(lst): return [x[:] for x in lst]   #Copy 2D list... Avoid Using Deepcopy
def no_of_digits(num): return 0 if num <= 0 else int(log10(num)) + 1
def powm(num, power, mod=M): return pow(num, power, mod)
def isPowerOfTwo(x): return (x and (not(x & (x - 1))))
def LSB(num):
    """Returns Least Significant Bit of a number (Rightmost bit) in O(1)"""
    return num & -num

def MSB(num):
    """Returns Most Significant Bit of a number (Leftmost bit) in O(logN)"""
    if num <= 0: return 0
    ans = 1; num >>= 1
    while num:
        num >>= 1; ans <<= 1
    return ans


LB = bisect_left   # Lower bound
UB = bisect_right  # Upper bound
 
def BS(a, x):      # Binary Search
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    else:
        return -1

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y)//gcd(x,y)


# import threading
# def dmain():
#     sys.setrecursionlimit(1000000)
#     threading.stack_size(1024000)
#     thread = threading.Thread(target=main)
#     thread.start()
            
# =============================== Custom Classes ===============================

class Wrapper(int):
    def __init__(self, x):
        int.__init__(x)
    def __hash__(self):
        return super(Wrapper, self).__hash__() ^ R
Int = lambda x:Wrapper(int(x))        

class myDict():
    def __init__(self,func=int):
        # self.RANDOM = randint(0,1<<32)
        self.RANDOM = R
        self.default=func
        self.dict={}
    def __getitem__(self,key):
        myKey=self.RANDOM^key
        if myKey not in self.dict:
            self.dict[myKey]=self.default()
        return self.dict[myKey]
    def __setitem__(self,key,item):
        myKey=self.RANDOM^key
        self.dict[myKey]=item
    def __contains__(self,key):
        myKey=self.RANDOM^key
        return myKey in self.dict
    def __delitem__(self,key):
        myKey=self.RANDOM^key
        del self.dict[myKey]
    def keys(self):
        return [self.RANDOM^i for i in self.dict]


# =============================== Region Fastio ===============================
if not os.path.isdir('C:/users/acer'):
    BUFSIZE = 8192
    
    
    class FastIO(IOBase):
        newlines = 0
    
        def __init__(self, file):
            self._fd = file.fileno()
            self.buffer = BytesIO()
            self.writable = "x" in file.mode or "r" not in file.mode
            self.write = self.buffer.write if self.writable else None
    
        def read(self):
            while True:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                if not b:
                    break
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines = 0
            return self.buffer.read()
    
        def readline(self):
            while self.newlines == 0:
                b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
                self.newlines = b.count(b"\n") + (not b)
                ptr = self.buffer.tell()
                self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
            self.newlines -= 1
            return self.buffer.readline()
    
        def flush(self):
            if self.writable:
                os.write(self._fd, self.buffer.getvalue())
                self.buffer.truncate(0), self.buffer.seek(0)
    
    
    class IOWrapper(IOBase):
        def __init__(self, file):
            self.buffer = FastIO(file)
            self.flush = self.buffer.flush
            self.writable = self.buffer.writable
            self.write = lambda s: self.buffer.write(s.encode("ascii"))
            self.read = lambda: self.buffer.read().decode("ascii")
            self.readline = lambda: self.buffer.readline().decode("ascii")
    
    
    def print(*args, **kwargs):
        """Prints the values to a stream, or to sys.stdout by default."""
        sep, file = kwargs.pop("sep", " "), kwargs.pop("file", sys.stdout)
        at_start = True
        for x in args:
            if not at_start:
                file.write(sep)
            file.write(str(x))
            at_start = False
        file.write(kwargs.pop("end", "\n"))
        if kwargs.pop("flush", False):
            file.flush()
    
    
    if sys.version_info[0] < 3:
        sys.stdin, sys.stdout = FastIO(sys.stdin), FastIO(sys.stdout)
    else:
        sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
    
    input = lambda: sys.stdin.readline().rstrip("\r\n")

# =============================== Endregion ===============================

if __name__ == "__main__":
    #read()
    main()
    #dmain()
