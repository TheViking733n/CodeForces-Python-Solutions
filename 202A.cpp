/**

Lexicographically Largest Palindromic Subsequence

 */


#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    vector<int> counter(26, 0);
    string s;
    int ind;

    cin>>s;

    for (char ch='a' ; ch<='z' ; ++ch)
    {
        ind = ch-97;
        for (int i=0 ; i<s.size() ; ++i)
        {
            if (ch == s[i])
            {
                counter[ind]++;
            }
        }
    }
    
    char letter;
    for(int i=25 ; i>=0 ; --i)
    {
        if (counter[i] != 0)
        {
            letter = (char)(97+i);
            for(int j=0 ; j<counter[i]  ; ++j)
                // cout<<i<<" "<<letter<<" "<<counter[i]<<"\n";
                cout<<letter;
                break;
        }
    }

    return 0;
}