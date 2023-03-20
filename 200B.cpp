#include <iostream>

using namespace std;

int main()
{
    int a, b, k2, k3, k5, k6;
    cin>>k2>>k3>>k5>>k6;

    a = min(min(k2, k5), k6);
    b = min(k3, k2-a);

    cout<<(256*a+32*b);

    return 0;
}