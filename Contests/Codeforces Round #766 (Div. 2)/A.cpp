#include <bits/stdc++.h>

using namespace std;

int main()
{
    vector<string> graph;
    string line;
    bool all_are_white;
    int t, n, m, r, c, ans;
    cin >> t;
    
    while (t--)
    {
        cin>>n>>m>>r>>c;
        graph = {};
        ans = 2;  // Default ans
        all_are_white = true;
        for (int i = 0; i<n; ++i)
        {
            cin>>line;
            graph.push_back(line);
            if(all_are_white && line.find('B')!=-1)
                all_are_white = false;

        }
        if (all_are_white)
            ans = -1;
        else if(graph[r-1][c-1]=='B')
            ans = 0;
        else
        {
            // Check horizontally
            line = graph[r-1];
            if (line.find('B')!=-1)
                ans = 1;

            else // Check vertically
            {
                for (int i=0; i<=n; ++i)
                {
                    if (graph[i][c-1] == 'B')
                    {
                        ans = 1;
                        break;
                    }
                }
            }


        }

        cout<<ans<<"\n";        
    }

    return 0;
}