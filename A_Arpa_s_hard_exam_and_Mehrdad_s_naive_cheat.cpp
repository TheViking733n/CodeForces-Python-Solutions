#include <iostream>

using namespace std;

int main()
{
    int n;
    cin>>n;
    
    if (n==0)
        printf("1");
    else
    {
        int arr[4] = {6, 8, 4, 2};
        int x = arr[n%4];
        cout<<x;
    }
        
    return 0;
}