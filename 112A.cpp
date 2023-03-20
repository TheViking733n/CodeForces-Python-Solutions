#include <iostream>
#include <string>

#define to_lower(ch) ch<97 ? ch+32 : ch


using namespace std;

int main()
{
    string a, b;
    char ch1, ch2;
    cin>>a>>b;
    int len = a.size();
    for(int i=0 ; i<len-1 ; ++i)
    {
        ch1 = to_lower(a[i]);
        ch2 = to_lower(b[i]);
        if(ch1>(ch2))
        {
            cout<<1;
            return 0;
        }
        else if(ch1<ch2)
        {
            cout<<-1;
            return 0;
        }
    }
    ch1 = to_lower(a[len-1]);
    ch2 = to_lower(b[len-1]);    
    if(ch1>ch2)
        cout<<1;
    else if(ch1<ch2)
        cout<<-1;
    else
        cout<<0;

    return 0;
}