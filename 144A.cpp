/**
Arrival of the General

A Ministryb for Defense sent a general to inspect the Super Secret Military Squad under the command of the Colonel SuperDuper.
Having learned the news, the colonel ordered to all n squad soldiers to line up on the parade ground.

*/

#include <iostream>

using namespace std;

int main()
{
    int x, n, max_ind, min_ind;
    cin>>n;
    int max=0, min = 101;
    for (int i=0 ; i<n ; ++i)
    {
        cin>>x;
        if (x>max){
            max = x;
            max_ind = i;
        }
        if (x<=min)
        {
            min = x;
            min_ind = i;
        }
    }

    cout<<(max_ind + n - 1 - min_ind - (max_ind>min_ind));
    
    return 0;
}