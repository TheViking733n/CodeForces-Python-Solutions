/**

System of Equations

Furik loves math lessons very much, so he doesn't attend them, unlike Rubik.
But now Furik wants to get a good mark for math. For that Ms. Ivanova, his math teacher,
gave him a new task. Furik solved the task immediately. Can you?

a + b^2 = n
a^2 + b = m



Approach:
Since a and b are integers, so n-b and m-a must be a perfect square

Therefore,
n-b=i^2 => b=n-i^2 ; i will go from 0 to (int)sqrt(n)
=> a = i

m-i should also be a perfect square
m>=i

*/


#include <iostream>
#include <cmath>

using namespace std;

bool is_perfect_sq(float num)
{
    if (num<0) return false;

    float root = sqrt(num);
    return (root - (int)root)==0;
}

int main()
{
    int n, m, sq_root, c=0;
    float temp;

    cin>>n>>m;
    sq_root = (int)sqrt(n);

    for(int i=0 ; i<=sq_root ; ++i)
    {
        // a = i ; b = n-i*i;
        if (is_perfect_sq(m-i) && (n-i*i)*(n-i*i) == (m-i))
        {
            // cout<<i<<" "<<(n-i*i)<<"\n";
            c++;
        }
    }

    cout<<c;

    return 0;
}



