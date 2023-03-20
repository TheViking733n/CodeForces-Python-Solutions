#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> time;
    vector<int> hp;
    
    int t, n, k, h, k_prev, h_prev, ans, t1, cur_time, cur_damage, cur_hp, delay, prev_damage, prev_damage_ind;
    cin >> t;
    
    while (t--)
    {
        cin>>n;
        
        time = {};
        hp = {};
        ans = 0;

        for (int i = 0; i < n; ++i)    
        {
            cin>>k;
            time.push_back(k);
        }
        
        for (int i = 0; i < n; ++i)    
        {
            cin>>h;
            hp.push_back(h);
        }

        t1 = time[n-1] - hp[n-1];
        
        prev_damage = hp[n-1];
        prev_damage_ind = n-1;
        ans += prev_damage*(prev_damage+1)/2;

        for (int i = n-2; i >=0 ; --i)
        {
            cur_time = time[i];
            delay = time[prev_damage_ind] - cur_time;
            cur_damage =prev_damage - delay;
            if (cur_damage <= 0){
                cur_damage = 0;
            }
            cur_hp = hp[i];

            if (cur_damage < cur_hp)
            {
                // Fire again
                if (cur_damage==0)
                {
                    prev_damage = cur_hp;
                    prev_damage_ind = i;
                    ans += prev_damage*(prev_damage+1)/2;
                }
                else
                {
                    // Remove prev fire value and add another value to
                    ans -= prev_damage*(prev_damage+1)/2;
                    
                    prev_damage = cur_hp + delay;

                    ans += prev_damage*(prev_damage+1)/2;

                }
            }
            


        }

        cout<<ans<<"\n";  
        
    }

    return 0;
}