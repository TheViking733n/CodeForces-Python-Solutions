x =  "3 2 1 0"

arr = [int(i) for i in x.split()]

for i in arr:
    b = bin(i)[2:]
    b = "0"*(4-len(b))+b
    print(b)