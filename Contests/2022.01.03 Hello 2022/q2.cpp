

#include <iostream>

using namespace std;

int main()
{
    int t, n, l, r, c, lower, upper, lower_price, upper_price, spent, spent_if_same;
    bool lower_and_upper_same;
    cin >> t;
    while (t--)
    {
        cin>>n>>l>>r>>c;
        lower = l;
        upper = r;
        spent = c;
        lower_price = c;
        upper_price = c;
        lower_and_upper_same = false;
         

        cout<<spent<<"\n";
        for(int i=1 ; i<n ; ++i)
        {
            cin>>l>>r>>c;
            if(lower>l &&  upper<r)
            {
                lower_and_upper_same = true;
                spent_if_same = c;
            }
            else if (lower==l &&  upper==r)
            {
                if (lower_and_upper_same)
                {
                    if (spent_if_same>c)
                        spent_if_same = c;
                }
                else
                {
                    // Checking which is better deal
                    if (spent > c)
                    {
                        lower_and_upper_same = true;
                        spent_if_same = c;
                    }                    
                }
            }
            else if (lower)
            {
                
            }
        }





    }
    return 0;
}   