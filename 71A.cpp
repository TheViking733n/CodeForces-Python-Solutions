/**
Way Too Long Words

Sometimes some words like "localization" or "internationalization"
are so long that writing them many times in one text is quite tiresome.
*/




#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n, len;
    string word;
    cin>>n;

    for(int i=0 ; i<n ; ++i)
    {
        cin>>word;
        len = word.size();
        if (len>10)
        {
            printf("%c%d%c\n", word[0], len-2, word[len-1]);
        }
        else
        {
            cout<<word<<"\n";
        }
    }
    
    return 0;
}