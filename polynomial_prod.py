"""
Input:
Two lists containing float type numbers.
These lists denote the co-efficients of two polynomials P and Q.

Output:
A list containing P+Q. A list containing P-Q.
A list containing PQ (the product).

def Sum_poly(P, Q):
    "This should display the sum of two polynomials P
    and Q. Note that P and Q are lists"

def Diff_poly(P, Q):
    "This should display the difference of two
    polynomials P and Q, that is (P-Q). Note that P and Q are lists"

def Prod_poly(P, Q):
    "This should display the product of two polynomials
    P and Q. Note that P and Q are lists"

Eg:
Input:
P=[1,2,3]
Q=(4,5,6)

Output:
Prod poly(PQ) should return the list [4,13,28,27.18]
"""



def Sum_poly(P, Q):
    """This should display the sum of two polynomials P
    and Q. Note that P and Q are lists"""
    len1, len2 = len(P), len(Q)
    ans = [0]*max(len1, len2)
    for i in range(-1, -len1-1, -1):
        ans[i] += P[i]
    for i in range(-1, -len2-1, -1):
        ans[i] += Q[i]
    return ans

def Diff_poly(P, Q):
    """This should display the difference of two
    polynomials P and Q, that is (P-Q). Note that P and Q are lists"""
    len1, len2 = len(P), len(Q)
    ans = [0]*max(len1, len2)
    for i in range(-1, -len1-1, -1):
        ans[i] += P[i]
    for i in range(-1, -len2-1, -1):
        ans[i] -= Q[i]
    return ans

def Prod_poly(P, Q):
    """This should display the product of two polynomials
    P and Q. Note that P and Q are lists"""
    len1, len2 = len(P), len(Q)
    ans = [0]*(len1+len2-1)
    for i in range(-1, -len1-1, -1):
        for j in range(-1, -len2-1, -1):
            ans[i+j+1] += P[i]*Q[j]
    return ans


if __name__ == "__main__":
    P = [1, 2, 3]
    Q = [4, 5, 6]
    print("Sum: P+Q =", Sum_poly(P, Q))
    print("Difference: P-Q =", Diff_poly(P, Q))
    print("Product: P*Q =", Prod_poly(P, Q))
