

#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> L;
    vector<int> R;
    vector<int> C;
    int t, n, l, r, c, lower, upper, lower_price, upper_price, spent, spent_if_same;
    bool lower_and_upper_same;
    cin >> t;
    while (t--)
    {
        cin>>n>>l>>r>>c;

        L={}; R={} ; C={};
        L.push_back(l);
        R.push_back(r);
        C.push_back(c);

        cout<<c<<"\n";

        for(int i=1 ; i<n ; ++i)
        {
            cin>>l>>r>>c;
            
            lower


            L.push_back(l);
            R.push_back(r);
            C.push_back(c);

            for(int i=1 ; i<n ; ++i)



        }





    }
    return 0;
}   