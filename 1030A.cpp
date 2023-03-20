/**
 
 In Search of an Easy Problem 
 
 if any of the person enters 1, print HARD else EASY
 */


#include <iostream>

using namespace std;

int main()
{
    int n, choice;
    cin>>n;
    for(int i=0 ; i<n ; ++i)
    {
        cin>>choice;
        if (choice==1)
        {
            cout<<"HARD";
            return 0;
        }
    }
    
    cout<<"EASY";   
    return 0;
}