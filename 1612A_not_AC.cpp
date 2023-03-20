/**
Manhattan distance between two points
 */

#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

void swap(int *xp, int *yp)
{
    int temp = *xp;
    *xp = *yp;
    *yp = temp;
}

int main(){
    int n, x, y;
    vector<int> x_arr;
    vector<int> y_arr;
    cin>>n;
    for(int i = 0 ; i < n ; ++i){
        cin>>x>>y;
        x_arr.push_back(x);
        y_arr.push_back(y);
    }

    for(int i = 0 ; i < n ; ++i){
        x = x_arr[i];
        y = y_arr[i];
        if(x%2==0 && y%2==0) // Both Even
        {
            cout<<(x/2)<<" "<<(y/2)<<"\n";
        }
        else if ((x%2==1 && y%2==0) || (x%2==0 && y%2==1))  // One is even, other is odd
        {   
            cout<<"-1 -1\n";
        }
        else
        {
            if (y>x)
            {
                swap(x,y);
            }
            // float a = (float)x/2, b = (float)y/2;
            // cout<<a<<" "<<b<<"\n";
            cout<<(y)<<" "<<((x-y)/2)<<"\n";
        }
    }
    return 0;

}

