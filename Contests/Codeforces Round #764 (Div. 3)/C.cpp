#include <bits/stdc++.h>

using namespace std;

bool finder_fun(int num, vector<int> left)
{
    if (left.size() == 1) // base case
    {
        return true;
    }
    
    int m;
    
    for (int i = 0; i < left.size(); ++i)
    {
        m = left[i];
        while (m>1)
        {
            if (m == num)
            {
                // Recursive call to this funtion

                vector<int> left_arr{left};  // Deep copy

                left_arr.erase(left_arr.begin() + i);

                if (finder_fun(num-1, left_arr))
                {
                    return true;
                }

                break;
            }
            m = m>>1;
        }
    }
    return false;
}

int main()
{
    vector<int> arr;
    int t, n, a;
    cin >> t;
    while (t--)
    {
        arr = {};
        cin >> n;
        for (int i=0 ; i<n; ++i)
        {
            cin>>a;
            arr.push_back(a);
        }

        // Sorting the array in decreasing order
        sort(arr.begin(), arr.end(), greater<int>());

        if (finder_fun(n, arr))
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
        
    }

    return 0;
}
