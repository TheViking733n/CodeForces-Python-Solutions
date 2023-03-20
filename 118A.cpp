/**

String Task

Petya started to attend programming lessons.
On the first lesson his task was to write a simple program.
The program was supposed to do the following: in the given string,
consisting if uppercase and lowercase Latin letters, it:

1) deletes all the vowels,
2) inserts a character "." before each consonant,
3) replaces all uppercase consonants with corresponding lowercase ones.

*/


#include <iostream>
#include <string>
#include <cctype>

using namespace std;

int main()
{
    string word;
    cin>>word;

    for(int i=0 ; i<word.size() ; ++i)
    {
        char ch = tolower(word[i]);
        if (ch!='a' && ch!='e' && ch!='i' && ch!='o' && ch!='u' && ch!='y')
        {
            printf(".%c", ch);
        }
    }

    return 0;
}