#include <iostream>

using namespace std;

int main()
{
    int n, a, b;
    cin>>n;
    int max = 0;
    int total = 0;
    while (n---1)
    {
        cin>>a>>b;
        total += b-a;
        if (total>max)
            max = total;
    }

    cout<<max;

    return 0;
}