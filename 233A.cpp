/**

Perfect Permutation

A permutation is a sequence of integers p1, p2, ..., pn, consisting of n distinct positive integers, each of them doesn't exceed n.
Let's denote the i-th element of permutation p as pi. We'll call number n the size of permutation p1, p2, ..., pn.

Nickolas adores permutations. He likes some permutations more than the others. He calls such permutations perfect.
A perfect permutation is such permutation p that for any i (1 ≤ i ≤ n) (n is the permutation size) the following equations hold ppi = i and pi ≠ i.
Nickolas asks you to print any perfect permutation of size n for the given n.

 */


#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;

    if (n==1 || n%2)
    {
        cout<<-1;
    }
    else
    {
        for(int i=1 ; i<=n/2 ; ++i)
        {
            printf("%d %d ", 2*i, 2*i-1);
        }
    }
 

    return 0;
}


