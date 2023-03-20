/**
Presents

Little Petya very much likes gifts.
Recently he has received a new laptop as a New Year gift from his mother.
He immediately decided to give it to somebody else as what can be more pleasant than giving somebody gifts.
And on this occasion he organized a New Year party at his place and invited n his friends there.

*/


#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n, x;
    cin>>n;
    vector<int> arr(n+1,-1);

    for(int i=1; i<=n ; i++)
    {
        cin>>x;
        arr[x]=i;
    }
    
    for(int i=1; i<=n ; i++)
    {
        printf("%d ", arr[i]);
    }

    return 0;
}