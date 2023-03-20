#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<pair<int,int>> arr;
    vector<int> A;
    
    int n, t, k, a, b;

    cin>>t;
    while(t--)
    {
        arr = {};
        A = {};
        cin>>n>>k;
        for (int i=0; i<n; ++i)
        {
            cin>>a;
            A.push_back(a);
        }
        
        for (int i=0; i<n; ++i)
        {
            cin>>b;
            arr.push_back( make_pair(A[i],b) );  
        }

        sort(arr.begin(), arr.end());

        for (int i=0; i<n; ++i)
        {
            a = arr[i].first; b = arr[i].second;
            if (k>=a)
            {
                k+=b;
            }
            else
            {
                break;
            }
        }

        printf("%d\n", k);
    }
    




    return 0;
}