/**

Team

One day three best friends Petya, Vasya and Tonya decided to form a team and take part in programming contests.
Participants are usually offered several problems during programming contests.
Long before the start the friends decided that they will implement a problem if at least two of them are sure about the solution.
Otherwise, the friends won't write the problem's solution.

 */


#include <iostream>

using namespace std;

int main()
{
    int n, a, b, c, count=0;
    cin>>n;
    for(int i=0 ; i<n ; ++i)
    {
        cin >> a >> b >> c;
        if (a+b+c >= 2)
            count++;
    }
    cout<<count;   

    return 0;
}