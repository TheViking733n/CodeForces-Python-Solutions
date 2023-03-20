# Programmer: The Viking
# Date: 19.08.2022


from collections import Counter
a = [int(i) for i in input("Enter array: ").split()]
f,fi = Counter(a),{a[i]:i for i in range(len(a)-1,-1,-1)}
print(*[i[2] for i in sorted([(-f[i], fi[i], i) for i in f])])