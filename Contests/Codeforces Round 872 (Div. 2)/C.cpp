#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define pb push_back
#define fr_z(start,end) for(int z=start;z<end;z++)
#define w while
#define mod 1300031
#define mp make_pair
#define fa_io std::ios::sync_with_stdio(false) //just for fast i/o

#define N 50100 //size of graph
#define root 1 //root of dfs tree

vector< pair<int,int> > g[N]; //pair.first=node,pair.second-cost
int subsize[N],n; //subsize[N] contains subsize of each node in dfs tree
ll res;

void dfs(int node,int cost,int parent)
{
    subsize[node]=1; //subsize of each node starts with one
    //cout<<node<<' '<<parent<<'\n';
    for(auto it:g[node])
    {
        int next=it.first;
        int c=it.second;
        if(next!=parent)
        {
            dfs(next,c,node);
            subsize[node]+=subsize[next]; //subsize[node]+=(subsize[of all of it's child node)
        }
    }
    res=( (((((ll)(n-subsize[node])%mod) * ((ll)subsize[node]%mod))%mod) * (((ll)cost)%mod))%mod + res%mod)%mod; //this is the same formula as given by you above, so THANX for it :)
}

int main()
{
    fa_io;
    cin.tie(NULL);
    int t=1,a,b,c;
    // cin>>t; //no. of testcases
    while(t--)
    {
        cin>>n; //no of nodes
        fr_z(1,n)
        {
            cin>>a>>b;
            c = 1;
            g[a].pb(mp(b,c));
            g[b].pb(mp(a,c)); //hope you get this in case if you don't comment or text me i'll explain
        }
        res=0;
        dfs(root,0,-1);
        fr_z(1,n+1)
            g[z].clear();
        

        cout <<res <<endl;
    }

    return 0;
}