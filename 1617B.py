"""
This is not a solution to the problem
I wrote this code only to check my approach to the problem

"""

def gcd(a,b):
    if b==0:
        return a
    return gcd(b, a%b)


for n in range(11, 30, 2):
    print()

# n = 11

    for i in range(1,n):
        for j in range(i, n):
            c = gcd(i,j)
            if i+j+c == n and c==1:
                print(i, j, c, n, sep="\t")
                # if (i, j, c) == my_ans:
                #     print(n, True)
                #     break