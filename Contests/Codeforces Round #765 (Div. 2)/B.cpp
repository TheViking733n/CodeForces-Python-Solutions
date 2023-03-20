#include <bits/stdc++.h>

using namespace std;

int main()
{

    unordered_map<int, vector<int> > index;
    
    int t, n, a, max_ans, ans, len, num, i1, i2, i3;
    cin >> t;
    while (t--)
    {

        index.clear();
        
        cin>>n;
        for (int i=0; i<n; i++)
        {
            cin>>a;
            index[a].push_back(i);
        }
        
        max_ans = -1;

        for (auto items : index)
        {
            num = items.first;
            len = items.second.size(); // len is the no. of repetitions of num

            if (len < 2) continue;

            for (int i=0; i<len-1; ++i)
            {
                i1 = items.second[i];
                i2 = items.second[i+1];

                ans = n-i2+i1;
                
                if(ans>max_ans)
                    max_ans = ans;
            }

        }

        cout<<max_ans<<"\n";

    }

    return 0;
}