
facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200]


for f in facts:
    print(bin(f)[2:])



g = {}

def fun(facts, i, cnt, mx, s):
    if i == len(facts):
        return
    
    if cnt == mx and s<=1e12:
        if bin(s).count('1') > mx:
            g[s] = mx

    
    # Take
    fun(facts, i+1, cnt+1, mx, s+facts[i])
    
    # Don't take
    fun(facts, i+1, cnt, mx, s)

for i in range(len(facts), 0, -1):
    fun(facts, 0, 0, i, 0)

# fun(facts, 0, 0, 8, 0)

print(len(g))

# for i in range(1, 3):
#     for m,c in g.items():
#         if i==c:
#             print(m,c)