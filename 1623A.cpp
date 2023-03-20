/**

Robot Cleaner
A robot cleaner is placed on the floor of a rectangle room, surrounded by walls.



Approach:
Find relative position of the dirt, whether it is in I Quard, II or III or IV

NOTE: HERE COORINATE SYSTEM IS INVERTED, i.e. y => -y

*/


#include <iostream>

using namespace std;

int main()
{
    int t, n, m, x0, y0, x1, y1, x, y, a, b;
    cin>>t;
    while(t--)
    {
        cin>>n>>m>>x0>>y0>>x1>>y1;
        // Changing values to zero based
        // --n; --m; --x0; --y0; --x1; --y1;

        // Relative position wrt to cleaner
        x = x1-x0;
        y = y1-y0;

        if (x==0 || y==0)
        {
            a = 0;
            b = 0;
        }

        else if (x>0 && y>0)  // I Quardrant
        {
            a = x;
            b = y;
        }
        else if (x<0 && y>0) // II Quadrant
        {
            a = 2*m - x1 - x0;
            b = y;
        }
        
        else if (x>0 && y<0) // IV Quadrant
        {
            a = x;
            b = 2*n - y1 - y0;
        }
        else // III Quadrant
        {
            a = 2*m - x1 - x0;
            b = 2*n - y1 - y0;
        }

        cout<<(min(a,b))<<"\n";
    }


    return 0;
}