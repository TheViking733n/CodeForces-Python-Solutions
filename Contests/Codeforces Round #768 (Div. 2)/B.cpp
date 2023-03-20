#include <bits/stdc++.h>

using namespace std;

void print_vector(vector<int> vec)
{
    for (auto it : vec)
        cout << it << " ";
    cout<<"\n";
}

int main()
{

    vector<int> arr;
    int b, a, n, t, a_max, b_max, am, bm, z, ans, right, left, cur;

    cin>>t;

    while(t--)
    {
        ans = 0;
        arr = {};
        cin>>n;
        for(int i=0; i<n; ++i)
        {
            cin>>a;
            arr.push_back(a);
        }

        if (n == 1){
            printf("0\n");
            continue;
        }
        if (n == 2){
            ans = (arr[0]!=arr[1]);
            printf("%d\n", ans);
            continue;
        }

        int j;

        for (int i=n-1; i>0;)
        {
            cur = arr[i];
            
            left = 0;
            for (j = i-1; j>=0; --j)
            {
                if (arr[j]==cur)
                    --i;
                else
                    break;
            }


            // Abb jo i ki value h, uspe aur uske right may jitne bhi elements h wo must be equal to cur


            if (i==0) break;

            cur = arr[i];
            right = n-i;

            
            // Abb given operation lagate h
            ++ans;

            for (j = i-1; j>=0 && right>0; --j)
            {
                arr[j] = cur;
                
                --right;
            }

            i = j+1;
            // cout<<ans<<"  i = "<<i<<"  arr = ";
            // print_vector(arr);

        }

        printf("%d\n", ans);

       
    }


    return 0;
}
