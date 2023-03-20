/**
 Theatre Square in the capital city of Berland has a rectangular shape with the size n × m meters.
 On the occasion of the city's anniversary,
 a decision was taken to pave the Square with square granite flagstones.
 Each flagstone is of the size a × a.

What is the least number of flagstones needed to pave the Square?
It's allowed to cover the surface larger than the Theatre Square,
but the Square has to be covered. It's not allowed to break the flagstones.
The sides of flagstones should be parallel to the sides of the Square.
 */

#include <iostream>
#include <cmath>

using namespace std;

// const int mod=1e9+7;

int main()
{
    long n, m, a;
    cin>>n>>m>>a;

    long long x = ceil((float)n/a);
    long long y = ceil((float)m/a);
    long long ans = x*y;//((x%mod)*(y%mod))%mod;
    cout<<ans;

    return 0;
}