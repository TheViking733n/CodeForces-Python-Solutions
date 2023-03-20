/*
GCD Problem

a + b + c = n
c = gcd(a,b)



Soltion:
if n is even then answer is (2, n-3, 1)
*/

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> primes{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229};

    int t, n, x;
    cin>>t;
    while (t--)
    {
        cin>>n;
        if (n%2 == 0)
        {
            printf("2 %d 1\n", n-3);
        }
        else
        {
            for(int i=1 ; i<1000 ; ++i)
            {
                x = primes[i];
                if ((n-x-1)%x)
                {
                    printf("%d %d 1\n", x, n-x-1);
                    break;
                }
            }
        }
    }

    return 0;
}

