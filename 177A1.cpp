/**

Good Matrix Elements

The Smart Beaver from ABBYY got hooked on square matrices. Now he is busy studying an n × n size matrix, where n is odd. The Smart Beaver considers the following matrix elements good:

Elements of the main diagonal.
Elements of the secondary diagonal.
Elements of the "middle" row — the row which has exactly (n-1)/2 rows above it and the same number of rows below it.
Elements of the "middle" column — the column that has exactly (n-1)/2 columns to the left of it and the same number of columns to the right of it.

*/

#include <iostream>

using namespace std;

int main()
{
    int n, x, sum=0;
    cin>>n;

    for (int i=0 ; i<n ; ++i)
    {
        for (int j=0 ; j<n ; ++j)
        {
            cin>>x;
            if (i==j || i==n-j-1 || i==(n-1)/2 || j==(n-1)/2) sum += x;
        }
    }


    cout<<sum;
    return 0;
}