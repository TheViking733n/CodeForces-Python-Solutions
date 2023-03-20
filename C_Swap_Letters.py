I = lambda: int(input())
LI = lambda: [int(i) for i in input().split()]

tt = 1
for _ in range(tt):
 n = I()
 a = input()
 b = input()
 i1, i2 = [], []
 for i in range(n):
  ch = a[i] + b[i]
  if ch == 'ab':
   i1.append(i)
  elif ch == 'ba':
   i2.append(i)
 ans = []
 while len(i1) > 1:
  ans.append((i1.pop(), i1.pop()))
 while len(i2) > 1:
  ans.append((i2.pop(), i2.pop()))
 if len(i1) ^ len(i2):
  print(-1)
  continue
 elif i1 and i2:
  ans.append((i1[0], i1[0]))
  ans.append((i1[0], i2[0]))
 print(len(ans))
 for i in ans: print(*[i[0] + 1, i[1] + 1])