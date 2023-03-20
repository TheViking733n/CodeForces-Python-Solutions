/**

A permutation of length n

n -> even

Input-> n a b

 */


#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

void solve(int n, int a, int b)
{
    vector<int> left = {a};
    vector<int> right = {b};
    

    if (min(a,b) <= n/2 && max(a,b) > n/2)
    {
        for(int i = 1 ; i<=n ; ++i)
        {
            if (i>n/2)
            {
                if (i>a && b!=i){
                    left.push_back(i);
                }
                else if (i<b && a!=i){
                    right.push_back(i);
                }
            }
            else
            {
                if (i<b && a!=i){
                    right.push_back(i);
                }
                else if (i>a && b!=i){
                    left.push_back(i);
                }
            }
        }
        
        if (left.size() + right.size() == n)
        {
            for(int i = 0 ; i < left.size() ; ++i) cout<<left[i]<<" ";
            for(int i = 0 ; i < right.size() ; ++i) cout<<right[i]<<" ";
            cout<<"\n";
        }
        else
            cout<<"-1\n";

    }
    else
        cout<<"-1\n";
}

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

int main()
{
    int T, N, A, B;
    cin>>T;
    for(int i = 0 ; i < T ; ++i)
    {
        cin>>N>>A>>B;
        solve(N, A, B);
    }
    return 0;
}