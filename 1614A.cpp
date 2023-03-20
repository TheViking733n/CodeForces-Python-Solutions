/**

Divan and a Store

Businessman Divan loves chocolate! Today he came to a store to buy some chocolate.
Like all businessmen, Divan knows the value of money, so he will not buy too expensive chocolate.
At the same time, too cheap chocolate tastes bad, so he will not buy it as well.

The store he came to has n different chocolate bars, and the price of the i-th chocolate bar is ai dollars.
Divan considers a chocolate bar too expensive if it costs strictly more than r dollars.
Similarly, he considers a bar of chocolate to be too cheap if it costs strictly less than l dollars.
Divan will not buy too cheap or too expensive bars.

Divan is not going to spend all his money on chocolate bars, so he will spend at most k dollars on chocolates.

Please determine the maximum number of chocolate bars Divan can buy.


n-> chocolates
a[i] is its price
if a[i] > r -> costly
if a[i] < l -> cheap

 */


#include <bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, l, r, budget, price;
    cin>>t;

    while(t--)
    {
        vector<int> a;
        cin>>n>>l>>r>>budget;

        for(int i=0 ; i<n ; ++i)
        {
            cin>>price;
            if(l<=price && price<=r)
                a.push_back(price);
        }

        sort(a.begin(), a.end());

        int i=0, count=0;
        while (budget>0 && i<a.size())
        {
            price = a[i];
            if(budget>=price)
            {
                ++count;
                budget-=price;
                ++i;
            }
            else
            {
                break;
            }
        }
        
        cout<<count<<"\n";
    }

    return 0;
}