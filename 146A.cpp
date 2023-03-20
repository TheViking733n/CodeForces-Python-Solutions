/**
Lucky Ticket

Petya loves lucky numbers very much.
Everybody knows that lucky numbers are positive integers whose decimal record contains only the lucky digits 4 and 7.
For example, numbers 47, 744, 4 are lucky and 5, 17, 467 are not.


Algo:
take input char by char
if any input is not 4 or 7-> print("NO") -> exit
make 4 count variables
left_4s, left_7s, right_4s and right_7s;

*/

#include <iostream>

using namespace std;

int main()
{
    int n;
    char ch;
    int left_4s=0, left_7s=0, right_4s=0, right_7s=0;
    
    cin>>n;

    for(int i=0 ; i<n/2 ; ++i)
    {
        cin>>ch;
        if (ch=='4')
            ++left_4s;
        else if(ch=='7')
            ++left_7s;
        else
        {
            cout<<"NO";
            return 0;
        }
    }
    
    for(int i=0 ; i<n/2 ; ++i)
    {
        cin>>ch;
        if (ch=='4')
            ++right_4s;
        else if(ch=='7')
            ++right_7s;
        else
        {
            cout<<"NO";
            return 0;
        }
    }

    if(left_4s == right_4s && left_7s == right_7s)
        cout<<"YES";
    else
        cout<<"NO";

    return 0;
}