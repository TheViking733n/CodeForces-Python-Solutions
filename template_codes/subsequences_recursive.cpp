#include <bits/stdc++.h>

using namespace std;

vector<int> arr;

void all_subseq(vector<int> &ds, int i)
{
    if (i == arr.size())
    {
        for (int i = 0; i < ds.size(); i++)
        {
            cout << ds[i] << " ";
        }
        cout << endl;
        return;
    }

    ds.push_back(arr[i]);
    all_subseq(ds, i + 1);
    ds.pop_back();
    all_subseq(ds, i + 1);
}

int main()
{
    arr = {1, 2, 3, 4};
    vector<int> ele;
    all_subseq(ele, 0);
    return 0;
}