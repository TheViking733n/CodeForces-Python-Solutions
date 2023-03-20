#include <bits/stdc++.h>

using namespace std;







/**

NOTE

insert_sorted() is not working


 */












void print_vector(vector<int> vec)
{
    for (auto it : vec)
        cout << it << " ";
    cout<<"\n";
}



void insert_sorted(vector<int> vec, int num)
{
    int len = vec.size();
    if (len==0)
    {
        vec.push_back(num);
        return;
    }
    else
    {
        int left=0, right=len-1;
        int mid, pos=-1;

        while (left<right)
        {
            mid = (left+right) / 2;
            // printf("%d %d %d\n", left, mid, right);
            
            if(num==mid)
            {
                pos = mid;
                break;
            }
            else if(num<mid)
            {
                right = mid-1;
            }
            else
            {
                left = mid+1;
            }
        }

        if (pos==-1) pos = left;

        vec.insert(vec.begin() + pos-1, num);

        print_vector(vec);

    }
}



int main()
{
    vector<int> v = {1,2};
    insert_sorted(v, 6);
    // print_vector(v);

    // cout<<"Program ran correctly";
    return 0;
}