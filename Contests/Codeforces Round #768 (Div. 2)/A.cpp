#include <bits/stdc++.h>

using namespace std;

int main()
{

    vector<int> A;
    int b, a, n, t, a_max, b_max, am, bm, z, ans;

    cin>>t;

    while(t--)
    {
        A = {};
        cin>>n;
        for(int i=0; i<n; ++i)
        {
            cin>>a;
            A.push_back(a);
        }

        a = A[0];
        cin>>b;

    
        a_max = min(a,b);

        b_max = a+b-a_max;

        for(int i=1; i<n; ++i)
        {
            a = A[i];
            cin>>b;

            am = min(a,b);
            bm = a+b-am;

            if (am>a_max) a_max = am;
            if (bm>b_max) b_max = bm;
           
        }

        cout<<(a_max*b_max)<<"\n";



       
    }


    return 0;
}
