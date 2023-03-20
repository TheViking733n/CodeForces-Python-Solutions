#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n, x, a, b, count;

    cin>>n;

    if(n==1)
    {
        cout<<0;
        return 0;
    }

    cin>>a>>b;

    count = (a==b) ? (0) : (1);

    int best=max(a,b), worst=min(a,b);

    for(int i=2 ; i<n ; i++)
    {
        cin>>x;
        if (x>best)
        {   
            best=x;
            count++;
        }
        else if(x<worst)
        {
            worst=x;
            count++;
        }
    }

    cout<<count;

    return 0;
}