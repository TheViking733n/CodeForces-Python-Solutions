/**

Series of Crimes

The Berland capital is shaken with three bold crimes committed by the Pihsters, a notorious criminal gang.

The Berland capital's map is represented by an n × m rectangular table.
Each cell of the table on the map represents some districts of the capital.

The capital's main detective Polycarpus took a map and
marked there the districts where the first three robberies had been committed as asterisks.
Deduction tells Polycarpus that the fourth robbery will be committed in such district,
that all four robbed districts will form the vertices of some rectangle, parallel to the sides of the map.

 */


#include <iostream>
#include <vector>

using namespace std;

int main()
{
    vector<int> x_coor;
    vector<int> y_coor;
    int x_max, y_max, x, y;
    cin>>y_max>>x_max;
    char ch;

    for(int j=0 ; j<y_max ; ++j)
    {
        for(int i=0 ; i<x_max ; ++i)
        {
            cin>>ch;
            if (ch=='*')
            {
                x_coor.push_back(i);
                y_coor.push_back(j);
            }
        }
    }
    
    if (x_coor[0]==x_coor[1]) x=x_coor[2];
    else if (x_coor[1]==x_coor[2]) x=x_coor[0];
    else if (x_coor[2]==x_coor[0]) x=x_coor[1];

    if (y_coor[0]==y_coor[1]) y=y_coor[2];
    else if (y_coor[0]==y_coor[1]) y=y_coor[2];
    else if (y_coor[1]==y_coor[2]) y=y_coor[0];
    
    printf("%d %d", y+1, x+1);
    return 0;
}