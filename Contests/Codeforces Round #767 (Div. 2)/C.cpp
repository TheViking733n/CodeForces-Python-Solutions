#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> B;
    vector<int> arr;
    unordered_map<int, vector<int>, greater<int>> dict;
    
    int n, t, a, b, cur_max;

    cin>>t;
    while(t--)
    {
        // missing.empty();
        dict.empty();
        B = {};
        cur_max = 0;

        cin>>n;
        for (int i=0; i<n; ++i)
        {
            cin>>a;
            if (dict.find(a) == dict.end())
            {
                arr = {i};
            }
            else
            {
                dict.insert(make_pair(a, i));
                arr = dict[a];
                arr.push_back(i);
            }

            dict.insert(make_pair(a, arr));

        }

        for (auto it:dict)
        {
            a = it.first;
            arr = it.second;
        }
        



    }

    return 0;
}